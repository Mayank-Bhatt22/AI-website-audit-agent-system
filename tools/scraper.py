import requests
from bs4 import BeautifulSoup


def scrape_website(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    return {
        "title": soup.title.string if soup.title else "",
        "text": soup.get_text(),
        "links": [a.get("href") for a in soup.find_all("a", href=True)],
    }