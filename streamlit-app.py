import os
os.environ["OPENAI_API_KEY"] = "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"

import openai
import streamlit as st

# Authenticate OpenAI API Key
openai.api_key = "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"

# Define the search_in_gpt3 function
def search_in_gpt3(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Answer the query with very accurate data gathered from most authentic sources of pathology. Use markdown syntax for styling. Query:"{query}"',
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        temperature=0.01,
    )
    return response.choices[0].text

# Set up the form
st.title("PARAG: Pathology AI Research Assistant with GPT4")
st.markdown("**Pathology education powered by AI**")
query = st.text_input("Search anything related to pathology:")
if st.button("Search with Chat GPT"):
    response = search_in_gpt3(query)
    st.markdown(response, unsafe_allow_html=True)
else:
    st.markdown("Your results appear here.")
    
