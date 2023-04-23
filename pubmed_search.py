import pymed

def pubmed_search(query):
    # Initialize the PubMed object
    p = pymed.PubMed()

    # Search for articles with the given query in their titles
    results = p.query(query, db='pmc', reldate=365)

    # Create a list of dictionaries with article titles and links
    articles = []
    for result in results:
        if query.lower() in result.title.lower():
            articles.append({
                'title': result.title,
                'link': f"https://www.ncbi.nlm.nih.gov/pmc/articles/{result.pmc}"
            })

    return articles
