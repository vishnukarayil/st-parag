import openai
import streamlit as st
import os

from pubmed_search import pubmed_search

# Set the page title and icon
favicon_path = os.path.join(os.path.dirname(__file__), 'cropped-PathonotesLogowithin.png')
st.set_page_config(page_title="PARAG - Pathology AI Research Assistant", page_icon=favicon_path)
disclaimer = """
### Disclaimer

PARAG is an educational tool that uses the GPT-3.5 language model developed by OpenAI to provide users with information related to pathology. Since this is an alpha release, the language model is still learning, and the responses can be edgy at times. We always recommend the use of standard literatures for more accurate answers. Use at your own risk.
        
The app name and all it's components are owned by the developer. We follow the ethics trained by our Mentors at GMC, Trivandrum, hence believe in ***Open Source*** & free education. The full code is accessible at GitHub.

"""

# Authenticate OpenAI API Key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Defining variables and arrays
list_options = {"Doubt (Ask as if you are asking a real Person)":"" , "Definition":"A standard definition followed by a brief description of" , "Essay":"A structured detailed essay on"}

# Define the search_in_gpt3 function
def search_in_gpt3(query,query_type):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'respond like an AI assistant for pathology research. We need it to generate factually correct answers for queries submitted by the user. User is a student in pathology and his questions are all related to pathology. The api will be used in a web app that is accessed in the pathology library pc in our medical college. There is no room for error. A single instance of a grossly wrong fact will ruin our reputation. So first, the api should cross check whether the question is correct. If the user ask about a made up word which is not a recognizable disease, you should ask the user to rephrase the question. Use markdown syntax for styling. Use headings wherever necessary. \n\nQuery: {query_type} of {query}\n\nResponse:',
        max_tokens=1024,
        top_p=1,
        n=1,
        frequency_penalty=0,
        presence_penalty=0,
        temperature=0.7,
    )
    return response.choices[0].text

# Set up the form
st.title("PARAG: Pathology AI Research Assistant with GPT3 (v1.03m)")
st.markdown("Pathology education powered by **ChatGPT**")
col1, col2 = st.columns([3,1])
with col1:
        query = st.text_input("Question / Search term")   
with col2:
        query_type_option = st.selectbox(
                'Type of question',
                list(list_options.keys()))
        query_type = list_options[query_type_option]
        
if st.button("PMC Articles"):
    article_links = pubmed_search(search_term=query, search_db="pmc", retmax=10)
    st.markdown(article_links)

if st.button("Search"):
    response = search_in_gpt3(query,query_type)
    st.markdown(response, unsafe_allow_html=True)
else:
    st.markdown("## [ Your result appears here ]")
    st.markdown(disclaimer)

    
# Add the static footer
st.markdown(
    """
    ---
    Copyright © 2023

    Proudly powered with [PathoNotes](https://pathonotes.com/wp/) by **Dr. Vishnu K R**
    """
)
