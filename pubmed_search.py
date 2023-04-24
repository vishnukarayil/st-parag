import requests
from bs4 import BeautifulSoup

def search_google_scholar(query):
    """
    Searches for a phrase in Google Scholar and returns a list of articles.
    """
    url = f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={query}&btnG="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    for result in soup.select(".gs_r"):
        title = result.select_one(".gs_rt a").text.strip()
        link = result.select_one(".gs_rt a")["href"]
        authors = result.select_one(".gs_a").text.strip()
        articles.append({"title": title, "link": link, "authors": authors})
    return articles
