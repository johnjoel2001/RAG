import pickle

INPUT_FILE = "chunk_text.pkl"
OUTPUT_FILE = "text_chunks.pkl"  # Stores chunked descriptions

def chunk_text(text_chunks, chunk_size=512):

    """Splits movie descriptions into fixed-sized chunks for retrieval"""

    chunked_texts = []
    for text in text_chunks:
        words = text.split()
        for i in range(0, len(words), chunk_size):
            chunked_texts.append(" ".join(words[i:i + chunk_size]))

    # Save chunked texts in root directory
    with open(OUTPUT_FILE, "wb") as f:
        pickle.dump(chunked_texts, f)

    print(f" Created {len(chunked_texts)} text chunks and saved to {OUTPUT_FILE}")
    return chunked_texts

if __name__ == "__main__":

    # Load extracted movie descriptions

    with open(INPUT_FILE, "rb") as f:
        text_chunks = pickle.load(f)

    chunk_text(text_chunks)
