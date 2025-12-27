## RTVSlo News Clustering and Visualization

This project focuses on clustering and visualizing news articles scraped from [rtvslo](https://www.rtvslo.si/). The goal is to explore the semantic structure of news content and present it in an interpretable, interactive visual form.

<img src="https://mpog.dev/content/uozp/clustering/final.png" style="width: 100%; max-width: 300px;" />

## Data Description

News articles were clustered based on their textual content, including:
- Titles
- Leads
- Full article paragraphs

Additionally, metadata about topics as defined on the MMC website was available. More fine-grained topics were extracted from article URLs. MMC topics were **not used during clustering**, but were later used for evaluation and comparison with the discovered clusters.

## Text Embeddings

Two substantially different embedding methods proved most relevant:

### TF-IDF
TF-IDF represents documents using word-frequency statistics. It produces high-dimensional sparse vectors and strictly separates different word forms. To reduce noise, articles were lemmatized before applying TF-IDF.

### SBERT
SBERT embeddings were computed without lemmatization, as contextual information benefits from different word forms. SBERT produces much lower-dimensional embeddings than TF-IDF but is computationally more expensive.

SBERT was selected for further work due to:
- Better suitability for semantic search
- Robustness to foreign languages
- Strong performance on large corpora
- TF-IDF remaining available for interpretability

## Dimensionality Reduction

Dimensionality reduction was applied to mitigate the curse of dimensionality and improve clustering quality.

- **UMAP (25D)** was used before clustering, as it preserves local (and partially global) structure and works well with SBERT embeddings.
- **t-SNE (2D)** was used only for visualization purposes. While effective at highlighting local structure, it can distort global distances and is unsuitable for clustering.
- SVD and PCA performed well on TF-IDF but poorly on SBERT due to nonlinearity.

Both UMAP and t-SNE are inherently nondeterministic.

## Clustering

The two best-performing clustering methods were:
- **DBSCAN**
- **k-means**

DBSCAN naturally discovers cluster counts and uses local density but leaves some points unassigned. k-means was chosen for the final solution because it is faster, assigns all points, and produces visually clear, globular clusters.

Cosine distance was preferred; where unsupported, Euclidean distance on normalized vectors was used.

The optimal number of clusters was determined using silhouette scores and interpretability, resulting in approximately **15–16 clusters**.

## Cluster Evaluation

Clusters were evaluated using both quantitative metrics and qualitative interpretability:
- Silhouette score
- Davies–Bouldin index
- Embedding alignment
- NPMI coherence
- ARI and NMI (only for comparison with MMC categories)

Interpretability and visual clarity were decisive factors in method selection.

## Cluster Explanation

Clusters are explained primarily through extracted keywords using:
- TF-IDF
- KeyBERT
- YAKE

NPMI was tested but excluded from the final visualization due to redundancy with TF-IDF. Texts were lemmatized and filtered using POS tagging (nouns, proper nouns, adjectives) via Stanza.

Large language models were tested for cluster summarization but discarded due to hallucinations and overfitting to representative samples.

## Visualization

Articles are displayed as points in a 2D embedding space, colored by cluster. Each cluster is enclosed by an ellipse computed via PCA with outlier resistance.

Clusters are labeled with their index and top TF-IDF keywords. Additional keyword explanations are shown on hover, and representative articles are available for inspection.

Users can toggle clusters, inspect overlaps, and assess relative distances interactively.

## Repository Structure

This repository contains everything needed to run the visualization and reproduce intermediate results.

### Directory Layout
- `cached/` – cached intermediate results
- `images/` – figures and visual outputs
- `workspace/` – development environment files (not part of final submission)
- `main.py` – entry point for running the visualization
- `predstavitev.pdf` – presentation of results
- `requirements.txt` – required Python dependencies

## Setup and Execution

The visualization is intended to run with **Python 3.12**.

Install dependencies:
```bash
pip install -r requirements.txt
