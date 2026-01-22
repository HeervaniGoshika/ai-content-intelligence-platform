import requests
from bs4 import BeautifulSoup

def load_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    return " ".join(p.text for p in soup.find_all("p"))