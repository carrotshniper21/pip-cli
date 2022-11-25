#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib

from selenium import webdriver
from selenium.webdriver import ChromeOptions
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re


def display_message():
    #
    print(''' \033[34m
   / __ \/  _/ __ \      / ____/ /   /  _/
  / /_/ // // /_/ /_____/ /   / /    / /
 / ____// // ____/_____/ /___/ /____/ /
/_/   /___/_/          \____/_____/___/
      Made by eat my nuts#4595
         Credits to 4ce#6574
    \033[0m  ''')


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

	if internet_working():
		# choose browser firefox or chrome
		print("Choose browser:\n1. Firefox\n2. Chrome")
		browser_choice = input("Enter choice: ")
		if browser_choice == "1" or browser_choice == "firefox":
			web_driver = setup_firefox()
		elif input == "2" or browser_choice == "chrome":
			web_driver = setup_chrome()
		else:
			print("Invalid input cannot setup web_driver")
			return
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
		# prefix = "https://vipstream.tv"
		# full_movie_paths = [prefix + movie for movie in movies]

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
	user_movie_choice = input("Choose movie: ")
	while not user_movie_choice.isdigit():
		print("Invalid choice, try again")
		user_movie_choice = input("Choose movie: ")
	user_movie_choice = convert_to_int(user_movie_choice)

	# get movie url
	movie_url = "https://vipstream.tv" + movies[user_movie_choice - 1]
	print(movie_url)

	web_driver_soft_close(web_driver)


if __name__ == '__main__':
	main()
