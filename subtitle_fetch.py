import requests
import zipfile
from pyfzf.pyfzf import FzfPrompt
from lxml import html
from bs4 import BeautifulSoup
import httplib2
import os

print(
    """
    __________ _________    ____  ________  __
   / ___/ ___// ____/   |  / __ \/ ____/ / / /
    \__ \\__ \/ __/ / /| | / /_/ / /   / /_/ /
  ___/ /__/ / /___/ ___ |/ _, _/ /___/ __  /
 /____/____/_____/_/  |_/_/ |_|\____/_/ /_/
                                                \n"""
)
web_url = "https://subscene.com"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"
}


def search_subtitles(name):
    url = f"{web_url}/subtitles/searchbytitle"
    r = requests.post(url, headers=headers, params={"query": name})
    if r.status_code == 200:
        return r.content


def parse_html(content):
    soup = BeautifulSoup(content, "lxml")
    return soup


def extract_links(soup):
    subtitle_links = []

    for a in soup.find_all("a"):
        href = a.get("href")
        if href:
            subtitle_links.append(href)

    return subtitle_links


print("Search Subtitles: ")
search_string = input("\n")
content = search_subtitles(search_string)
soup = parse_html(content)
subs = extract_links(soup)
subs = list(set([i for i in subs if i.startswith("/subtitles/")]))

fzf = FzfPrompt()


def display_subtitle_links(subs):
    choice = []

    for sub in subs:
        choice.append("https://subscene.com" + sub)

    selected = fzf.prompt(subs)
    sub_url = "https://subscene.com" + "".join(selected)
    return sub_url


sub_url = display_subtitle_links(subs)


def parse_url(sub_url):
    l = requests.get(sub_url, headers=headers)
    if l.status_code == 200:
        soup = BeautifulSoup(l.content, "lxml")
        links = []
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.startswith("/subtitles/"):
                links.append("https://subscene.com" + "".join(href))
        return links


links = parse_url(sub_url)
selected_url = fzf.prompt(links)

file_names = []
file_names.append("".join(selected_url))

for file_name in file_names:
    file_name = file_name.replace("\r", "").replace("\n", "").strip()

    resp, content = httplib2.Http().request(file_name)

    if resp.status == 200:
        objlxml = html.fromstring(content)

        filename = "subtitle"

        print("Downloading %s ..." % filename)

        btnEl = objlxml.xpath("//a[@id='downloadButton']")

        if len(btnEl):
            downloadUrl = btnEl[0].get("href")

            resp, zipcontent = httplib2.Http().request(
                "http://subscene.com" + downloadUrl
            )

            if resp.status == 200:
                with open(filename + ".zip", "wb") as fw:
                    fw.write(zipcontent)

                with zipfile.ZipFile(f"{filename}.zip", "r") as zip_ref:
                    zip_ref.extractall()

                os.remove(f"{filename}.zip")

                print("...%s done!\n" % filename)
