from Bio import Entrez
import streamlit as st

def pubmed_search(search_term, search_db="pmc", retmax=10):
    # Set the email address associated with your NCBI account
    Entrez.email = "vishnu.karayil@gmail.com"

    # Perform the search
    handle = Entrez.esearch(db=search_db, term=search_term, retmax=retmax)
    record = Entrez.read(handle)

    # Get the list of article IDs from the search results
    article_ids = record["IdList"]

    # Create an empty list to hold the article titles and URLs
    article_links = []

    # Loop through the article IDs and retrieve the article information
    for article_id in article_ids:
        # Get the article information from Pubmed Central
        article_handle = Entrez.efetch(db=search_db, id=article_id, retmode="xml")
        article_record = Entrez.read(article_handle)[0]
        article_handle.close()

        # Extract the article title and URL from the article information
        try:
            article_title = article_record["PubmedArticle"]["MedlineCitation"]["Article"]["ArticleTitle"]
        except KeyError:
            article_title = article_record["PubmedArticle"]["Article"]["ArticleTitle"]
        article_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{article_id}/"

        # Add the article title and URL to the list of article links
        article_links.append((article_title, article_url))

    # Display the list of article links
    for article_title, article_url in article_links:
        st.write(f"[{article_title}]({article_url})")
