# import streamlit as st
# from generate_response import generate_response 

# #  Streamlit UI Configuration
# st.set_page_config(page_title="Movie AI Assistant", page_icon="🎬", layout="wide")

# # Securely Load OpenAI API Key
# try:
#     OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
# except KeyError:
#     st.error("OpenAI API key is missing! Please add it to Streamlit secrets.")

# #  Header
# st.markdown("<h1 style='text-align: center;'> Movie AI Assistant</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; font-size: 18px;'>Ask anything about movies, genres, directors, and recommendations!</p>", unsafe_allow_html=True)

# # Sidebar Theme Customization
# with st.sidebar:
#     st.markdown("##  Customize Theme")
#     theme_color = st.color_picker("Pick a theme color", "#4B9CD3")

#     # Apply the selected theme color to the page
#     st.markdown(
#         f"""
#         <style>
#         .stButton>button {{ background-color: {theme_color}; color: white; border-radius: 8px; }}
#         .stTextInput>div>div>input {{ border-color: {theme_color}; }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# #  Search Section
# st.markdown("### 🔍 Ask a movie-related question:")
# query = st.text_input("Enter your question:", key="query")

# #  Display Sample Prompts (Static Text)
# st.markdown("#### 🔹 Try asking:")
# st.markdown("- Recommend an action movie")
# st.markdown("- What are the best thriller movies?")
# st.markdown("- Who directed Inception?")
# st.markdown("- What are the best sci-fi movies of all time?")
# st.markdown("- What are some underrated movies?")

# #  Get Answer Button with Styling
# if st.button(" Get Answer"):
#     if query:
#         with st.spinner(" Thinking..."):
#             ai_response = generate_response(query)  #  Calls GPT for response

#         # Improved UI: AI Response in a Stylish Card
#         st.markdown("""
#         <style>
#             .response-box {
#                 background-color: #ffffff;
#                 color: #333;
#                 padding: 15px;
#                 border-radius: 10px;
#                 box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
#                 font-size: 18px;
#                 line-height: 1.6;
#             }
#         </style>
#         """, unsafe_allow_html=True)

#         #  Display AI-generated answer inside a styled box
#         st.markdown(f'<div class="response-box">{ai_response}</div>', unsafe_allow_html=True)

#     else:
#         st.warning(" Please enter a question before clicking 'Get Answer'.")

import streamlit as st
from generate_response import generate_response 

#  Streamlit UI Configuration
st.set_page_config(page_title="Movie AI Assistant", page_icon="🎬", layout="wide")

# Securely Load OpenAI API Key
try:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
except KeyError:
    st.error("OpenAI API key is missing! Please add it to Streamlit secrets.")

#  Header
st.markdown("<h1 style='text-align: center;'> Movie AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Ask anything about movies, genres, directors, and recommendations!</p>", unsafe_allow_html=True)

# Sidebar Theme Customization
with st.sidebar:
    st.markdown("##  Customize Theme")
    theme_color = st.color_picker("Pick a theme color", "#4B9CD3")

    # Apply the selected theme color to the page
    st.markdown(
        f"""
        <style>
        .stButton>button {{ background-color: {theme_color}; color: white; border-radius: 8px; }}
        .stTextInput>div>div>input {{ border-color: {theme_color}; }}
        </style>
        """,
        unsafe_allow_html=True
    )

#  Search Section
st.markdown("### 🔍 Ask a movie-related question:")
query = st.text_input("Enter your question:", key="query")

#  Display Sample Prompts (Static Text)
st.markdown("#### 🔹 Try asking:")
st.markdown("- Recommend an action movie")
st.markdown("- What are the best thriller movies?")
st.markdown("- Who directed Inception?")
st.markdown("- What are the best sci-fi movies of all time?")
st.markdown("- What are some underrated movies?")

#  Get Answer Button with Styling
if st.button(" Get Answer"):
    if query:
        with st.spinner(" Thinking..."):
            ai_response = generate_response(query)  #  Calls GPT for response

        # Improved UI: AI Response in a Stylish Card
        st.markdown("""
        <style>
            .response-box {
                background-color: #ffffff;
                color: #333;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                font-size: 18px;
                line-height: 1.6;
            }
        </style>
        """, unsafe_allow_html=True)

        #  Display AI-generated answer inside a styled box
        st.markdown(f'<div class="response-box">{ai_response}</div>', unsafe_allow_html=True)

    else:
        st.warning(" Please enter a question before clicking 'Get Answer'.")
