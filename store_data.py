import faiss
import numpy as np
import pickle
import os
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA


EMBEDDINGS_FILE = "embeddings.pkl"
FAISS_INDEX_FILE = "faiss_movie_index.bin"
PCA_MODEL_FILE = "pca_model.pkl"
TEXT_CHUNKS_FILE = "text_chunks.pkl"  

def store_embeddings(text_chunks, model_name="all-MiniLM-L6-v2"):
    """Generate embeddings and store them in FAISS."""

    embedding_model = SentenceTransformer(model_name)

    # Generate embeddings
    embeddings = np.vstack([embedding_model.encode(text) for text in text_chunks])

    # Reduce dimensionality using PCA
    pca = PCA(n_components=128)
    reduced_embeddings = pca.fit_transform(embeddings)

    # Create FAISS index
    dimension = reduced_embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(reduced_embeddings)

    # Save PCA model, embeddings, and FAISS index in the root directory
    with open(EMBEDDINGS_FILE, "wb") as f:
        pickle.dump(reduced_embeddings, f)
    with open(PCA_MODEL_FILE, "wb") as f:
        pickle.dump(pca, f)
    faiss.write_index(faiss_index, FAISS_INDEX_FILE)

    print(f" Stored {len(reduced_embeddings)} embeddings and saved FAISS index.")

if __name__ == "__main__":
    # Load preprocessed text chunks
    with open(TEXT_CHUNKS_FILE, "rb") as f:
        text_chunks = pickle.load(f)

    store_embeddings(text_chunks)
