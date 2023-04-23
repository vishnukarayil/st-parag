import requests
import xml.etree.ElementTree as ET

def search_pubmed(query, databases=['pmc', 'pubmed']):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    db_param = ",".join(databases)
    search_url = base_url + f"esearch.fcgi?db={db_param}&retmax=10&term=" + query
    search_result = requests.get(search_url)
    root = ET.fromstring(search_result.content)
    id_list = []
    for id in root.findall("./IdList/Id"):
        id_list.append(id.text)
    results = []
    for id in id_list:
        for db in databases:
            summary_url = base_url + f"esummary.fcgi?db={db}&id=" + id
            summary_result = requests.get(summary_url)
            root = ET.fromstring(summary_result.content)
            title = root.find(f"./DocSum/Item[@Name='Title']").text
            link = f"https://www.ncbi.nlm.nih.gov/{db}/{id}"
            if query.lower() in title.lower():
                results.append({'title': title, 'link': link})
                break
    return results
