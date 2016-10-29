import cfscrape
from bs4 import BeautifulSoup

scraper = cfscrape.create_scraper()

def search(keyword):
    content = scraper.post("http://kissanime.to/Search/Anime", data={'keyword': 'hunter'}).content

    soup = BeautifulSoup(content, 'html.parser')

    list_series = soup.find("table", "listing")
    links = list_series.find_all('a')

    series = []

    for a in links:
        series.append((a.string, a['href']))

    return series


print(search("hunter"))