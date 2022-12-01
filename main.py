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

def get_subtitle_count(subs):
    return len(subs)

def validate_user_subtitle_choice(user_choice, subs):
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

if __name__ == '__main__':
    main(subs)
