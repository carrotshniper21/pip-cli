#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import urllib

from selenium import webdriver
from selenium.webdriver import ChromeOptions
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def display_message():
    os.system('''
COLOR='\033[1;31m'
NC='\033[0m' # No Color
cat << EOF
${COLOR}
   / __ \/  _/ __ \      / ____/ /   /  _/
  / /_/ // // /_/ /_____/ /   / /    / /
 / ____// // ____/_____/ /___/ /____/ /
/_/   /___/_/          \____/_____/___/
       Made by eat my nuts#4595
          Credits to 4ce#6574
${NC}
EOF''')


BASE_URL = "https://vipstream.tv/home"


# genres = genres.replace("https://vipstream.tv/genre/", "")


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


# ALMOST DONE Create an object to hold list of genres and links
# TODO 2D array of movie titles and links
# TODO Finding the download link

def get_url_source(url, browser_headless):
    browser_headless.get(url)
    page_source = browser_headless.page_source
    browser_headless.close()
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


def movies_from_genre(web_driver, user_choice):
    movies = web_driver.find_elements(By.XPATH, "//a[@href]")
    movie_links = []
    for movie in movies:
        link = movie.get_attribute('href')
        if 'genre' in movie.get_attribute('href'):
            return movie_links


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
    loading_message()

    if internet_working():
        web_driver = setup_firefox()
        genre_links = get_genres(web_driver)
        display_genres_to_user(genre_links)
        user_choice = get_user_genre_choice(1, get_genre_count(genre_links))
        print("User choice: ", user_choice)
        # loop until user enters valid choice
        while not validate_user_genre_choice(user_choice, genre_links):
            print("Invalid choice, try again")
            user_choice = get_user_genre_choice(1, get_genre_count(genre_links))
        user_choice = convert_to_int(user_choice)

        web_driver.get(genre_links[user_choice - 1])
        movie_links = movies_from_genre(web_driver, user_choice)
        parse_movies(movie_links)

        Finally: web_driver_soft_close(web_driver)
    else:
        print("No internet connection")


if __name__ == '__main__':
    main()
