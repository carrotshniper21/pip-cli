import requests
import bs4
import fuzzywuzzy as fw


web_url = "https://subscene.com"
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"}

def search_subtitles(name):
    url = f"{web_url}/subtitles/searchbytitle"
    r = requests.post(url, headers=headers, params={'query': name})
    if r.status_code == 200:
        return r.content

def parse_html(content):
    soup = bs4.BeautifulSoup(content, 'lxml')
    return soup

def extract_links(soup):
    subtitle_links = []

    for i in soup.findAll('a'):
        subtitle_links.append(i.get('href'))
    return subtitle_links

def fuzzy_match(search_string, subs_list):
    # import fuzzywuzzy

    fw.fuzz.ratio(search_string, subs_list)
    # return the closest match
    return fw.process.extractOne(search_string, subs_list)

search_string = input("Search Subtitles: ")
content = search_subtitles(search_string)
soup = parse_html(content)
subs = extract_links(soup)
subs = list(set([i for i in subs if i.startswith('/subtitles')]))

#subs = fuzzy_match(search_string, subs

def display_subtitle_links(sub):
    for i, sub in enumerate(subs, start = 1):
        print(i, sub)
display_subtitle_links(subs)
