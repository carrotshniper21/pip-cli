from selenium.webdriver.common.by import By
import re


def get_genres(web_driver):
	elems = web_driver.find_elements(By.XPATH, "//a[@href]")
	links = []
	for elem in elems:
		link = elem.get_attribute('href')
		if 'genre' in elem.get_attribute('href'):
			links.append(link)
	return links


def validate_user_genre_choice(user_choice, genre_links):
	if user_choice.isdigit():
		if 1 <= int(user_choice) <= get_genre_count(genre_links):
			return True
		else:
			return False
	else:
		return False


def display_genres_to_user(genre_links):
	for i, link in enumerate(genre_links):
		print(i + 1, link.replace("https://vipstream.tv/genre/", ""))


def get_user_genre_choice(start_choice, last_choice):
	return input(f'\nChoose genre ({start_choice}-{last_choice}): ')


def get_genre_count(links):
	return len(links)


def parse_movies(movie_links):
	for movie in movie_links:
		print(movie)


def get_url_source(url, browser_headless):
	browser_headless.get(url)
	page_source = browser_headless.page_source
	return page_source


def get_movie_src(genre_links, user_choice, web_driver):
	return get_url_source(genre_links[user_choice - 1], web_driver)


def get_movies_from_genre(movie_src):
	# get movies from genre
	regex = re.compile(r'href="(.+?)"')
	regex2 = re.compile(r'/movie/.+?')
	movies = regex.findall(movie_src)
	movies = list(filter(regex2.search, movies))
	movies = list(dict.fromkeys(movies))
	return movies
