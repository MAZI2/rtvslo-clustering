[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/BqdZfKWE)
Ta datoteka naj opiše strukturo vašega repozitorija.

Vsebuje naj tudi vse potrebne informacije za zagon rešitve ter tudi, kako bi lahko poustvarili vse vmesne rezultate. Ne pozabite na seznam potrebnih knjižnic.

### Evaluation scripts

# ----------- SBERT Embeddings ----------- #
#print("Generating SBERT embeddings...")
#sbert_model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
#sbert_embeddings = sbert_model.encode(texts, batch_size=64, show_progress_bar=True)

#np.save('sbert_embeddings.npy', sbert_embeddings)

# ----------- SBERT Embeddings ----------- #
import stanza
from tqdm import tqdm
# Initialize Stanza pipeline for Slovene
stanza.download('sl')  # only once
nlp = stanza.Pipeline('sl', processors='tokenize,pos,lemma', use_gpu=False)

# -------------------------------
# Preprocess: Keep only NOUN, PROPN, ADJ
# -------------------------------
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


# Only preprocess once per article
preprocessed_texts = [preprocess_text(text) for text in tqdm(texts)]