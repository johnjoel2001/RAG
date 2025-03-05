import openai
from retrieve_data import retrieve_top_k  

# Securely load API key from Streamlit secrets
try:
    import streamlit as st
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
except KeyError:
    raise ValueError(" OpenAI API key is missing! Please add it to Streamlit secrets.")

#  Initialize OpenAI client (NEW API format)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_response(query):

    """Retrieves relevant movie descriptions and generates a response using GPT."""

    retrieved_context = "\n".join(retrieve_top_k(query, k=3))  # Retrieves actual text

    
    prompt = f"""
    Context: {retrieved_context}
    User Query: {query}
    AI Response:
    """

    try:
        #  Use OpenAI's NEW API format
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Change to "gpt-4-turbo" if needed
            messages=[
                {"role": "system", "content": "You are a movie expert."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content  # Extract response

    except Exception as e:
        return f" Error generating response: {str(e)}"

if __name__ == "__main__":
    query = "What are the best sci-fi movies?"
    response = generate_response(query)
    print(f"AI Response:\n{response}")
