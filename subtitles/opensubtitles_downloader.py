import pandas as pd
import requests
import zipfile
from iso639 import Lang
from pyfzf.pyfzf import FzfPrompt
from lxml import html
from bs4 import BeautifulSoup
import os


def get_media_name():
    return input("Enter a Movie/TV Show: ")


def get_language_choice():
    return input("Choose language: ")


def get_language_code(language_choice):
    if language_choice == "all":
        lg = "all"
    else:
        lg = Lang(language_choice.capitalize())
        lg = lg.pt3
    return lg


def get_xml_data(lg, media_name):
    url = f"https://www.opensubtitles.org/en/search/sublanguageid-{lg}/moviename-{media_name}/atom_1_00.xml"
    xml_data = requests.get(url).content
    return xml_data


media_name = get_media_name()
language_choice = get_language_choice()
language_code = get_language_code(language_choice)
xml_data = get_xml_data(language_code, media_name)
fzf = FzfPrompt()


def parse_xml(xml_data):
    soup = BeautifulSoup(xml_data, "xml")
    df = pd.DataFrame(columns=["title", "updated", "summary"])

    subtitle_links = []

    # Iterating through item tag and extracting elements
    all_items = soup.find_all("entry")
    items_length = len(all_items)

    for index, entry in enumerate(all_items):
        title = entry.find("title").text
        link = entry.find("link").get("href")
        updated = entry.find("updated").text
        summary = entry.find("summary").text

        subtitle_links.append(link)

        # Adding extracted elements to rows in table
        row = {"title": title, "updated": updated, "summary": summary}

        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

    return df, subtitle_links


df, subtitle_links = parse_xml(xml_data)
df.to_csv("subtitles.csv")

selected = fzf.prompt(subtitle_links)


def parse_url(selected):
    sub_url = "".join(selected)
    print("")

    try:
        response = requests.get(sub_url)
    except Exception as e:
        pass

    if response.status_code == 200:
        try:
            objlxml = html.fromstring(response.content)
        except Exception as e:
            pass

        filename = "subtitle"

        print("Downloading %s ..." % filename)

        btnEl = objlxml.xpath("//a[@id='bt-dwl-bt']")

        if len(btnEl):
            downloadUrl = btnEl[0].get("href")

            try:
                response = requests.get("https://www.opensubtitles.org" + downloadUrl)
            except Exception as e:
                pass

            if response.status_code == 200:
                with open(filename + ".zip", "wb") as f:
                    f.write(response.content)

                    print("...%s done!\n" % filename)

    with zipfile.ZipFile(f"{filename}.zip", "r") as zip_ref:
        file_names = [name for name in zip_ref.namelist() if not name.endswith(".nfo")]
        for file_name in file_names:
            zip_ref.extract(file_name)

    os.remove(f"{filename}.zip")


parse_url(selected)
