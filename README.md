Ta datoteka naj opiše strukturo vašega repozitorija.

Vsebuje naj tudi vse potrebne informacije za zagon rešitve ter tudi, kako bi lahko poustvarili vse vmesne rezultate. Ne pozabite na seznam potrebnih knjižnic.
## Struktura repozitorija
- ```cached/``` mapa z datotekami, ki vsebujejo vmesne rezultate
- ```images/``` mapa s slikami
- ```workspace/``` mapa z datotekami razvojnega okolja (ne predstavlja dela končne oddaje)
- ```main.py``` datoteka za zagon vizualizacije
- ```predstavitev.pdf``` pdf datoteka s predstavitvijo rezultatov 
- ```requirements.txt``` datoteka s potrebnimi knjižnicami 

## Zagon vizualizacije in vzpostavitev okolja
Vizualizacija je namenjena zagonu v `python 3.12`. Knjižnice, ki so potrebne za zagon namestimo z
```bash
pip install -r requirements.txt
```
Vizualizacijo zaženemo z datoteko `main.py`. Skripta uporablja že izračunane SBERT vložitve v datoteki `sbert_embeddings.npy` in preprocesirana besedila iz datoteke `preprocessed_combined.jsonl`. Brez podanih argumentov se uporabijo tudi že izračunane množice skupin in ključnih besed za vsako skupino.

Argumenti:
- `--no_cache`: ponovno se izračunajo skupine in ključne besede

Primeri:
```bash
python main.py
python main.py --no_cache
```

## Generiranje vmesnih rezultatov
### SBERT vložitve
file: ```cached/sbert_embeddings.npy```
#print("Generating SBERT embeddings...")
#sbert_model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
#sbert_embeddings = sbert_model.encode(texts, batch_size=64, show_progress_bar=True)

#np.save('sbert_embeddings.npy', sbert_embeddings)

### Preprocesiranje besedil
file: ```cached/preprocessed_combined.jsonl```\
\
Preprocesiranje besedil s Stanzo je precej računsko zahtevno. Zato je bilo opravljeno v kosih.


``` python 
import stanza
from tqdm import tqdm
import json
from pathlib import Path
import glob

articles = load_articles('articles.yaml')
texts = [get_article_text(article) for article in tqdm(articles, desc="Processing articles")]

stanza.download('sl')
nlp = stanza.Pipeline('sl', processors='tokenize,pos,lemma', use_gpu=True)

def preprocess_text(text):
    doc = nlp(text)
    tokens = []
    for sentence in doc.sentences:
        for word in sentence.words:
            if word.upos in ['NOUN', 'PROPN', 'ADJ']:
                lemma = word.lemma.lower()
                if len(lemma) > 2:
                    tokens.append(lemma)
    return ' '.join(tokens)

# Processing and Saving in Chunks
def preprocess_and_save(texts, batch_size=5000, output_prefix="preprocessed"):
    total = len(texts)
    for i in range(0, total, batch_size):
        chunk = texts[i:i + batch_size]
        processed = [preprocess_text(text) for text in tqdm(chunk, desc=f"Batch {i // batch_size}")]

        filename = f"{output_prefix}_{i // batch_size}.jsonl"
        with open(filename, "w", encoding="utf-8") as f:
            for line in processed:
                f.write(json.dumps(line, ensure_ascii=False) + "\n")

# Combining chunks
def combine_jsonl_files(output_prefix="preprocessed", combined_filename="combined.jsonl"):
    input_files = sorted(glob.glob(f"{output_prefix}_*.jsonl"))

    with open(combined_filename, "w", encoding="utf-8") as outfile:
        for fname in tqdm(input_files, desc="Combining files"):
            with open(fname, "r", encoding="utf-8") as infile:
                for line in infile:
                    outfile.write(line)


preprocess_and_save(texts)
combine_jsonl_files()
```

## Druge skripte
### Koda za evalvacijo metod
```python
import numpy as np
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    adjusted_rand_score,
    normalized_mutual_info_score,
)
from sklearn.metrics.pairwise import cosine_similarity
from gensim.corpora import Dictionary
from gensim.models import CoherenceModel
import pandas as pd
from tqdm import tqdm

# Import data
embeddings = np.load("umap_25d.npy")
clusters = np.load("sbert_clusters.npy")
true_labels = np.load("mmc_labels.npy")

def embedding_alignment_score(embeddings, labels):
    label_set = set(labels)
    if -1 in label_set:
        label_set.remove(-1)

    similarities = []
    for label in label_set:
        cluster_embeddings = embeddings[labels == label]
        if len(cluster_embeddings) < 2:
            continue
        sim_matrix = cosine_similarity(cluster_embeddings)
        upper_triangle = sim_matrix[np.triu_indices_from(sim_matrix, k=1)]
        similarities.append(np.mean(upper_triangle))

    return np.mean(similarities) if similarities else None

def evaluate_all(embeddings, clusters, label_name, tokenized_texts=None, true_labels=None):
    mask = clusters != -1
    # NPMI Coherence (based on tokenized_texts)
    if tokenized_texts is not None:
        dictionary = Dictionary(tokenized_texts)
        cluster_topics = []
        for cluster_id in np.unique(clusters):
            if cluster_id == -1:
                continue  # Skip noise
            docs = [tokenized_texts[i] for i in range(len(clusters)) if clusters[i] == cluster_id]
            if not docs:
                continue
            cluster_dictionary = Dictionary(docs)
            corpus = [cluster_dictionary.doc2bow(doc) for doc in docs]
            # Get top words for topic (just the dictionary keys sorted by frequency)
            word_freq = {}
            for doc in corpus:
                for word_id, freq in doc:
                    word_freq[word_id] = word_freq.get(word_id, 0) + freq
            sorted_words = sorted(word_freq.items(), key=lambda x: -x[1])
            topic_words = [cluster_dictionary[word_id] for word_id, _ in sorted_words[:10]]
            cluster_topics.append(topic_words)

        cm = CoherenceModel(
            topics=cluster_topics,
            texts=tokenized_texts,
            dictionary=dictionary,
            coherence='c_npmi'
        )
        avg_npmi = cm.get_coherence()
    else:
        avg_npmi = None
    metrics = {
        "Embedding": label_name,
        "Silhouette": silhouette_score(embeddings[mask], clusters[mask]) if np.sum(mask) > 1 else None,
        "Davies-Bouldin": davies_bouldin_score(embeddings[mask], clusters[mask]) if np.sum(mask) > 1 else None,
        "ARI": adjusted_rand_score(true_labels, clusters) if true_labels is not None else None,
        "NMI": normalized_mutual_info_score(true_labels, clusters) if true_labels is not None else None,
        "Num Clusters": len(set(clusters)) - (1 if -1 in clusters else 0),
        "Noise Points": np.sum(clusters == -1),
        "Embedding Alignment": embedding_alignment_score(embeddings, clusters),
        "Avg NPMI": avg_npmi
    }
    return metrics

# Evaluate both embeddings
print(evaluate_all(
    embeddings=sloberta_embeddings,
    clusters=sloberta_clusters,
    label_name="SBERT-KMEANS",
    tokenized_texts=tokenized_texts,
    true_labels=true_labels  # optional
))
```

### Koda za ekstrakcijo MMC kategorij
file: ```mmc_labels.npy```
```python 
from urllib.parse import urlparse
import re

def extract_topics_from_url(url, skip_last_n=2):
    path = urlparse(url).path
    parts = [part for part in path.strip("/").split("/") if part]

    if len(parts) > skip_last_n:
        topics = parts[:-skip_last_n]
    else:
        topics = []

    # Replace hyphens with spaces, remove numbers if needed, clean up
    topics = [re.sub(r'[-_]+', ' ', topic) for topic in topics]

    return topics

for article in articles:
    article['url_topics'] = extract_topics_from_url(article['url'])

mmc_labels = [
    "/".join(article['url_topics']) if article['url_topics'] else "no-topic"
    for article in articles
]
np.save("mmc_labels.npy", mmc_labels)
```
### Dodatne razlage skupin
