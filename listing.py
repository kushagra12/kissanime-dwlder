import cfscrape
from bs4 import BeautifulSoup
import bs4
import anime_dwlder

scraper = cfscrape.create_scraper()

def get_episodes(series_link):
    content = scraper.get(series_link, cookies={'username':'ahv%2f7hqvi8mpKbuCCUlMFriMbEiTxcRk', 'password': 'e2oS8nVOzxz0jbW9wecKghDFXSiCpJ%2bS'}).content

    soup = BeautifulSoup(content, 'html.parser')

    list_episdoes = soup.find("table", "listing")

    links = list_episdoes.find_all('a')

    episodes = []

    for a in links:
        episodes.append(a['href'])

    return episodes[::-1]


def get_links(episode_link, preferred_quality='1280x720'):
    content = scraper.get(episode_link,
                          cookies={'username': 'ahv%2f7hqvi8mpKbuCCUlMFriMbEiTxcRk',
                                   'password': 'e2oS8nVOzxz0jbW9wecKghDFXSiCpJ%2bS'}).content

    soup = BeautifulSoup(content, 'html.parser')

    download_links = soup.find('div', {'id': "divDownload"})

    links = download_links.find_all('a')

    episode = {}

    for a in links:
        if(a.string == preferred_quality + '.mp4'):
            episode['url'] = a['href']

    file_name = soup.find('div', {'id' : 'divFileName'})

    file_name = ''.join([t for t in file_name.contents if type(t)==bs4.element.NavigableString])

    episode['name'] = file_name.strip()

    return episode


episodes = get_episodes("http://kissanime.to/Anime/Akame-ga-Kill")

for e in episodes:
    anime_link = get_links('http://kissanime.to' + e)
    anime_dwlder.download_episode(anime_link['url'], anime_link['name'] + '.mp4', 'Akame ga Kill')

