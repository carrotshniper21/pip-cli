import requests
import bs4

root_url = "https://subscene.com"
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"}

def search_subtitles(name):
    url = f"{root_url}/subtitles/searchbytitle"
    r = requests.post(url, headers=headers, params={'query': name})
    if r.status_code == 200:
        return r.content


def parse_html(content):
    soup = bs4.BeautifulSoup(content, 'lxml')
    return soup


def extract_links(soup):
    for i in soup.findAll('a'):
        link = i.get('href')
        # text = i.text
        if link:
            print(link.replace("/subtitles/", ""), f"{link}")


content = search_subtitles("Doctor Strange")
soup = parse_html(content)
extract_links(soup)
