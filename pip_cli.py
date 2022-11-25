#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
import time
import urllib

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


def display_message():
    #
    os.system('\n'
              'COLOR=\'\033[1;31m\'\n'
              'NC=\'\033[0m\' # No Color\n'
              'cat << EOF\n'
              '${COLOR}\n'
              '   / __ \/  _/ __ \      / ____/ /   /  _/\n'
              '  / /_/ // // /_/ /_____/ /   / /    / /\n'
              ' / ____// // ____/_____/ /___/ /____/ /\n'
              '/_/   /___/_/          \____/_____/___/\n'
              '       Made by eat my nuts#4595\n'
              '          Credits to 4ce#6574\n'
              '${NC}\n'
              'EOF')


BASE_URL = "https://vipstream.tv/home"


def setup_firefox():
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver_f = webdriver.Firefox(options=options)
    driver_f.get(BASE_URL)
    return driver_f


def setup_chrome():
    opts = ChromeOptions()
    opts.headless = True
    chrome_headless = webdriver.Chrome(options=opts)
    return chrome_headless


def get_genres(web_driver):
    elems = web_driver.find_elements(By.XPATH, "//a[@href]")
    links = []
    for elem in elems:
        link = elem.get_attribute('href')
        if 'genre' in elem.get_attribute('href'):
            links.append(link)
    return links


def get_url_source(url, browser_headless):
    browser_headless.get(url)
    page_source = browser_headless.page_source
    return page_source


def write_to_file(page_source):
    with open('page_source.html', 'w') as f:
        f.write(page_source)


def internet_working():
    try:
        urllib.request.urlopen('https://google.com', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False


def display_genres_to_user(genre_links):
    for i, link in enumerate(genre_links):
        print(i + 1, link.replace("https://vipstream.tv/genre/", ""))


def get_user_genre_choice(start_choice, last_choice):
    return input(f'\nChoose genre ({start_choice}-{last_choice}): ')


# looking up https://docs.python.org/3/tutorial/inputoutput.html


def validate_user_genre_choice(user_choice, genre_links):
    if user_choice.isdigit():
        if 1 <= int(user_choice) <= get_genre_count(genre_links):
            return True
        else:
            return False
    else:
        return False


def convert_to_int(user_choice):
    return int(user_choice)


def get_genre_count(links):
    return len(links)


def parse_movies(movie_links):
    for movie in movie_links:
        print(movie)


def web_driver_soft_close(web_driver):
    try:
        web_driver.close()
    except:
        pass


def loading_message():
    print("Loading Selections...\n")


def main():
    display_message()
    prefix = "https://vipstream.tv"

    if internet_working():
        # choose browser firefox or chrome
        print("Choose browser:\n1. Firefox\n2. Chrome")
        browser_choice = input("Enter choice: ")
        # if browser choice is firefox
        if browser_choice == "1" or browser_choice == "firefox":
            web_driver = setup_firefox()
        # if browser choice is chrome
        elif input == "2" or browser_choice == "chrome":
            time.sleep(3)
            web_driver = setup_chrome()
        else:
            print("Invalid choice, defaulting to Firefox")
            web_driver = setup_firefox()
        loading_message()

        genre_links = get_genres(web_driver)
        display_genres_to_user(genre_links)

        user_choice = get_user_genre_choice(1, get_genre_count(genre_links))

        # loop until user enters valid choice
        while not validate_user_genre_choice(user_choice, genre_links):
            print("Invalid choice, try again")
            user_choice = get_user_genre_choice(1, get_genre_count(genre_links))
        user_choice = convert_to_int(user_choice)

        # get movies from genre
        regex = re.compile(r'href="(.+?)"')
        regex2 = re.compile(r'/movie/.+?')
        movie_src = get_url_source(genre_links[user_choice - 1], web_driver)
        movies = regex.findall(movie_src)
        movies = list(filter(regex2.search, movies))
        movies = list(dict.fromkeys(movies))

        # get movie titles
        regex3 = re.compile(r'<h2 class="film-name">.+?</h2>')
        titles = regex3.findall(movie_src)
        titles = [title.replace('<h2 class="film-name">', '').replace('</h2>', '') for title in titles]

        # titles = all title="(.+?)"
        regex4 = re.compile(r'title="(.+?)"')
        # titles to string
        titles = regex4.findall(str(titles))

        # display titles list to user

        for i, title in enumerate(titles):
            print(i + 1, title)

        # get user choice
        user_movie_choice = input(f"\nChoose movie(1-{len(titles)}): ")
        user_movie_choice = convert_to_int(user_movie_choice)
        # print("Loading Movies...")
        movie_url = prefix + movies[user_movie_choice - 1]
        movie_page_src = get_url_source(movie_url, web_driver)

        # <li class="nav-item">
        # <a class="nav-link btn btn-sm btn-secondary btn-radius link-item default" data-linkid="9086422" href="/watch-movie/watch-the-lair-full-89620.9086422"
        # id="watch-9086422"
        # onclick="watch(this,event)" title="Server UpCloud">
        # <i class="fas fa-play mr-2"></i><span>UpCloud</span>
        # </a>
        # </li>

        # get href from <a class="nav-link btn btn-sm btn-secondary btn-radius link-item default" data-linkid="9086422" href="/watch-movie/watch-the-lair-full-89620.9086422"

        regex5 = re.compile(r'href="(.+?)"')
        regex6 = re.compile(r'/watch-movie/.+?')
        movie_servers = regex5.findall(movie_page_src)
        movie_servers = list(filter(regex6.search, movie_servers))
        movie_servers = list(dict.fromkeys(movie_servers))
        movie_servers = [prefix + link for link in movie_servers]
        movie_servers.pop(0)
        # get server names from span
        regex7 = re.compile(r'<span>.+?</span>')
        server_names = regex7.findall(movie_page_src)
        # ['0.0', "If current server doesn't work please try other servers below.", 'UpCloud', 'Vidcloud', 'Streamlare', '2022', '80m', '2022', '99m', '2022', '84m', 'SS 1', 'EPS 1', '2022', '97m', '2022', '103m', '2022', '124m', '2022', '107m', '2022', '99m', 'SS 1', 'EPS 3', '2022', '102m', 'SS 1', 'EPS 4', '2022', '84m', 'SS 1', 'EPS 3', '2022', '87m', '2022', '95m']
        # refine server names ( there is only 3)
        server_names = [name.replace('<span>', '').replace('</span>', '') for name in server_names]
        server_names = server_names[2:5]
        server_choice = input(f"\nChoose server(1-{len(server_names)}): ")
        server_choice = convert_to_int(server_choice)
        server_url = movie_servers[server_choice - 1]
        server_page_src = get_url_source(server_url, web_driver)
        # save server page source to file
        write_to_file(server_page_src)
        print("finding video...")

        web_driver_soft_close(web_driver)


if __name__ == '__main__':
    main()
