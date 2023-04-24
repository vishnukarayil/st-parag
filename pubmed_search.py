import requests
import xml.etree.ElementTree as ET

def search_pubmed(query):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = base_url + "esearch.fcgi?db=pmc&retmax=500&term=" + query
    search_result = requests.get(search_url)
    root = ET.fromstring(search_result.content)
    id_list = []
    for id in root.findall("./IdList/Id"):
        id_list.append(id.text)
    results = []
    for id in id_list:
        summary_url = base_url + "esummary.fcgi?db=pmc&id=" + id
        summary_result = requests.get(summary_url)
        try:
            root = ET.fromstring(summary_result.content)
            title = root.find("./DocSum/Item[@Name='Title']").text
            link = "https://www.ncbi.nlm.nih.gov/pmc/articles/" + id
            if query.lower() in title.lower():
                results.append({'title': title, 'link': link})
        except ET.ParseError as e:
            print(f"Error parsing XML for article ID {id}: {e}")
    return results
