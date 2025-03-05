import pandas as pd
import json
import pickle
import os


DATA_FOLDER = "datasets/"  # Ensure all dataset files are inside this folder
SAVE_PATH = "text_chunks.pkl"  # Stores extracted movie descriptions

def load_movie_data():

    """Loads and preprocesses movie data from multiple CSV files."""

    # Load datasets
    movies_df = pd.read_csv(os.path.join(DATA_FOLDER, "movies_metadata.csv"), low_memory=False)
    credits_df = pd.read_csv(os.path.join(DATA_FOLDER, "credits.csv"))
    keywords_df = pd.read_csv(os.path.join(DATA_FOLDER, "keywords.csv"))

    #  Convert IDs to string for merging
    movies_df["id"] = movies_df["id"].astype(str)
    credits_df["id"] = credits_df["id"].astype(str)
    keywords_df["id"] = keywords_df["id"].astype(str)

    # Merge datasets
    movies_df = movies_df.merge(credits_df, on="id", how="left")
    movies_df = movies_df.merge(keywords_df, on="id", how="left")

    # Extract relevant fields
    def preprocess_movie_data(row):
        try:
            genres = ", ".join([g["name"] for g in json.loads(row["genres"].replace("'", '"'))])
        except:
            genres = "Unknown"
        try:
            keywords = ", ".join([k["name"] for k in json.loads(row["keywords"].replace("'", '"'))])
        except:
            keywords = "Unknown"
        try:
            crew = ", ".join([c["name"] for c in json.loads(row["crew"].replace("'", '"')) if c["job"] in ["Director", "Producer", "Writer"]])
        except:
            crew = "Unknown"

        return f"Title: {row['title']}\nOverview: {row['overview']}\nGenres: {genres}\nKeywords: {keywords}\nDirector/Producer: {crew}\nRelease Date: {row['release_date']}"

    # Create full movie descriptions
    movies_df["text_chunk"] = movies_df.apply(preprocess_movie_data, axis=1)
    text_chunks = movies_df["text_chunk"].tolist()

    # Save extracted descriptions in root directory
    with open(SAVE_PATH, "wb") as f:
        pickle.dump(text_chunks, f)

    print(f"Extracted {len(text_chunks)} movie descriptions and saved to {SAVE_PATH}")
    return text_chunks

if __name__ == "__main__":
    load_movie_data()
