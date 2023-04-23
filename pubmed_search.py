import requests
from urllib.parse import urlencode

def pubmed_search(query, retmax=10):
    """
    Search for articles in PubMed Central using a query term.

    Parameters:
    - query (str): The search term.
    - retmax (int): The maximum number of articles to return (default: 10).

    Returns:
    - article_links (str): A Markdown-formatted string containing links to the matching articles.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = base_url + "esearch.fcgi"

    # Build the query parameters
    params = {
        "db": "pmc",
        "term": query,
        "retmax": retmax,
        "retmode": "json"
    }

    # Make the API request
    response = requests.get(search_url + "?" + urlencode(params))

    # Parse the response JSON
    results = response.json()["esearchresult"]

    # Check for errors
    if "errorlist" in results:
        error = results["errorlist"]["error"][0]["message"]
        return f"Error: {error}"

    # Extract the PMIDs
    pmids = results["idlist"]

    # Build the article links
    article_links = f"This feature is coming soon"
    for pmid in pmids:
        link = f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmid}/"
        title = f"PMC{pmid}"
        article_links += f"- [{title}]({link})\n"

    return article_links
