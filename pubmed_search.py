import requests
from bs4 import BeautifulSoup

def search_doaj(query):
    url = f"https://doaj.org/api/v1/search/articles/oss?pageSize=1000&q=title%3A%22{query}%22"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    results = []
    for article in soup.find_all("article"):
        title = article.find("a", {"class": "title_link"}).text
        link = article.find("a", {"class": "title_link"})["href"]
        results.append({"title": title, "link": link})
    return results
