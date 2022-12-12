import requests
import bs4
import urllib

#import fuzzywuzzy as fw


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

#def fuzzy_match(search_string, subs_list):
#    import fuzzywuzzy

#    fw.fuzz.ratio(search_string, subs_list)
#    return the closest match
#    return fw.process.extractOne(search_string, subs_list)

search_string = input("Search Subtitles: ")
content = search_subtitles(search_string)
soup = parse_html(content)
subs = extract_links(soup)
subs = list(set([i for i in subs if i.startswith('/subtitles')]))

def get_subtitle_count(subs):
    return len(subs)

def validate_user_subtitle_choice(user_choice, subs):
    if isinstance(user_choice, int):
        user_choice = str(user_choice)
    if user_choice.isdigit():
        if 1 <= int(user_choice) <= get_subtitle_count(subs):
            return True
        else:
            return False
    else:
        return False

def convert_to_int(user_choice):
    return int(user_choice)

#subs = fuzzy_match(search_string, subs

def display_subtitle_links(sub):
    for i, sub in enumerate(subs):
        print(i + 1, sub.replace("/subtitles/", ""))
display_subtitle_links(subs)

def get_user_subtitle_choice(start_choice, last_choice):
    return input(f'\nChoose Subtitle ({start_choice}-{last_choice}): ')

def main(subs):
    user_choice = get_user_subtitle_choice(1, get_subtitle_count(subs))
    print('\n')

        # loop until user enters valid choice
    while not validate_user_subtitle_choice(user_choice, subs):
        print("Invalid choice, try again")
        user_choice = get_user_subtitle_choice(1, get_subtitle_count(subs))

    user_choice = convert_to_int(user_choice)
    idx = int(user_choice) - 1
    print(subs[idx])


if __name__ == '__main__':
    main(subs)

# from pyfzf.pyfzf import FzfPrompt
# from slowprint.slowprint import *
# from bs4 import BeautifulSoup
# from requests_html import HTMLSession
# import requests
# 
# print('''
#    __________ _________    ____  ________  __
#   / ___/ ___// ____/   |  / __ \/ ____/ / / /
#    \__ \\__ \/ __/ / /| | / /_/ / /   / /_/ / 
#  ___/ /__/ / /___/ ___ |/ _, _/ /___/ __  /  
# /____/____/_____/_/  |_/_/ |_|\____/_/ /_/   
#                                                \n''')
# web_url = "https://subscene.com"
# headers = {
#     'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"}
# 
# def search_subtitles(name):
#     url = f"{web_url}/subtitles/searchbytitle"
#     r = requests.post(url, headers=headers, params={'query': name})
#     if r.status_code == 200:
#         return r.content
# 
# def parse_html(content):
#     soup = BeautifulSoup(content, 'lxml')
#     return soup
# 
# def extract_links(soup):
#     subtitle_links = []
# 
#     for i in soup.findAll('a'):
#         subtitle_links.append(i.get('href'))
#     return subtitle_links
# 
# slowprint("Search Subtitles: ", 0.5)
# search_string = input("\n")
# content = search_subtitles(search_string)
# soup = parse_html(content)
# subs = extract_links(soup)
# subs = list(set([i for i in subs if i.startswith('/subtitles/')]))
# fzf = FzfPrompt()
# 
# def get_subtitle_count(subs):
#     return len(subs)
# 
# def validate_user_subtitle_choice(user_choice, subs):
#     if isinstance(user_choice, int):
#         user_choice = str(user_choice)
#     if user_choice.isdigit():
#         if 1 <= int(user_choice) <= get_subtitle_count(subs):
#             return True
#         else:
#             return False
#     else:
#         return False
# 
# def convert_to_int(user_choice):
#     return int(user_choice)
# 
# def display_subtitle_links(subs):
#     choice = []
#     for i, sub in enumerate(subs):
#         choice.append("{}. {}".format(i + 1, sub.replace("/subtitles/", "")))
# 
#     selected = fzf.prompt(choice)
# 
#     if selected in choice:
#         print(choice.index(selected))
# 
# display_subtitle_links(subs)
# 
# def main(selected, i):
#     session = HTMLSession()
#     r = session.get("https://subscene.com" + selected[0])
#     sub_links = list(r.html.absolute_links)
#     sub_links = list(set([r for r in sub_links if r.startswith('/subtitles/')]))
#     print(sub_links)
# 
# if __name__ == '__main__':
#     main(subs)
