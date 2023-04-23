from pyEntrez import entrez
import urllib.parse

def search_pmc_articles(query):
    # Initialize the Entrez object
    e = entrez()

    # Encode the query for use in the Entrez search API
    encoded_query = urllib.parse.quote(query)

    # Search for articles with the given query in their titles
    results = e.esearch(db='pmc', term=encoded_query, reldate=365)

    # Fetch the full records for the search results
    records = e.efetch(db='pmc', id=results.ids, rettype='medline', retmode='text')

    # Parse the records and extract the article titles and links
    articles = []
    for record in records:
        title = None
        link = None
        for line in record.split('\n'):
            if line.startswith('TI  - '):
                title = line[6:]
            elif line.startswith('PMCID- '):
                link = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{line[7:]}"
        if title is not None and link is not None:
            articles.append({'title': title, 'link': link})

    return articles
