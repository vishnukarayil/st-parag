from Bio import Entrez

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
        article_handle = Entrez.efetch(db=search_db, id=article_id, rettype="medline", retmode="text")
        article_record = article_handle.read()
        article_handle.close()

        # Extract the article title and URL from the article information
        article_title = article_record.split("\n")[1].strip()
        article_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{article_id}/"

        # Add the article title and URL to the list of article links
        article_links.append((article_title, article_url))

    return article_links
