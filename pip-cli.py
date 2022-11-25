#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib, re, os, subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

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
display_message()


BASE_URL = "https://vipstream.tv/home"

#genres = genres.replace("https://vipstream.tv/genre/", "")


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
# TODO 2d array of movie titles and links
# TODO Finding the download link

def get_url_source(BASE_URL, browser_headless):
    browser_headless.get(BASE_URL)
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
    for i in genre_links:
        print(genre_links(i))


def get_user_genre_choice(start_choice, last_choice):
    return input(f'Choose genre ({start_choice}-{last_choice} ): ')
    # looking up https://docs.python.org/3/tutorial/inputoutput.html


def get_genre_count(links):
    return len(links)

def load_genre(web_driver, user_choice):
    movies = web_driver.find_elements(By.XPATH, "//a[@href]")
    movie_links = []
    for movie in movies:
        link = movie.get_attribute('href')
        if 'genre' in movie.get_attribute('href'):
            return movie_links


# you shouldn't just delete all of the notes that help you remember what shit does
# instead you should rewrite or replace the comments with more summarized versions
# just keep it simple

# yeah this shit is starting to get confusing

def parse_movies(movie_links):
    print("ok")


def main():
    display_message()
    if internet_working():
        chrome = setup_chrome()
        links = get_genres(chrome)

        display_genres_to_user(links)

        # asking the user from dynamically counting the links
        choice = get_user_genre_choice(1, get_genre_count(links))
        # starting to user the driver to display list of movies from that ge
        load_genre(chrome, choice)

        try:
            chrome.close()
        except:
            pass

# this is only test code leave here


# case switch in python google
# also instead of typing the genre name you can just make the user choose a number
# starting from 0 - max_choice

# stop saying sorry and saying you're a noob
# just focus on what's happening with the code

# TODO: work on making chrome driver HEADLESS AGAIN!!!


# we need that datatype with all the links in the one array
# [link1,link2, link3]
# we use this datastructure then we just
#  check if choice is valid integer
# then webdriver.get(urls[choice])
# so how do we get the urls from the [link1, link2, link3]
# im just confused how we get the urls from the array
# choose any number from the array by taking the name of the array arrayName[number of item you want from array (0-arrayName(length))]

# so we get the integer input? like
# just normal user input
# check if its (1-28)
# if user didn't write 1-28 then show an error and tell the user to choose number between 1-28
# TODO: create a choice loop (retry function)
# worry about it LATER
# but make a note of what you want to do


