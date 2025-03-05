import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

#  Load stored FAISS index and data
FAISS_INDEX_FILE = "faiss_movie_index.bin"
EMBEDDINGS_FILE = "embeddings.pkl"
PCA_MODEL_FILE = "pca_model.pkl"
TEXT_CHUNKS_FILE = "text_chunks.pkl"

# Load text chunks (so we can return actual descriptions)
with open(TEXT_CHUNKS_FILE, "rb") as f:
    text_chunks = pickle.load(f)

# Load FAISS index
faiss_index = faiss.read_index(FAISS_INDEX_FILE)

# Load PCA model
with open(PCA_MODEL_FILE, "rb") as f:
    pca = pickle.load(f)

def retrieve_top_k(query, k=3, model_name="all-MiniLM-L6-v2"):

    """Retrieve relevant movie descriptions from FAISS."""

    embedding_model = SentenceTransformer(model_name)

    # Encode query and apply PCA
    query_embedding = np.array([embedding_model.encode(query)], dtype=np.float32)
    query_embedding = pca.transform(query_embedding)

    # Search FAISS index
    distances, indices = faiss_index.search(query_embedding, k)

    # Return actual movie descriptions instead of indices
    retrieved_texts = [text_chunks[i] for i in indices[0]]

    return retrieved_texts  # ✅ Now it returns a list of movie descriptions

if __name__ == "__main__":
    query = "best action movies"
    results = retrieve_top_k(query)
    print(f" Retrieved movies:\n{results}")
