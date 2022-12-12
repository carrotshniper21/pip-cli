from selenium.webdriver.common.by import By
import re
import emulation
import util


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

def get_movie_src(genre_links, user_choice, web_driver):
	return emulation.get_url_source(genre_links[user_choice - 1], web_driver)


def get_movies_from_genre(movie_src):
	# get movies from genre
	regex = re.compile(r'href="(.+?)"')
	regex2 = re.compile(r'/movie/.+?')
	movies = regex.findall(movie_src)
	movies = list(filter(regex2.search, movies))
	movies = list(dict.fromkeys(movies))
	return movies


def user_choice_validator_loop(user_choice, genre_links, web_driver):
    # loop until user enters valid choice
    while not validate_user_genre_choice(user_choice, genre_links):
        print("Invalid choice, try again")
        user_choice = get_user_genre_choice(1, movie.get_genre_count(genre_links))
    user_choice = util.convert_to_int(user_choice)

    movie_src = get_movie_src(genre_links, user_choice, web_driver)
    return get_movies_from_genre(movie_src), movie_src


def scrape_movie_titles(movie_src):
    # get movie titles
    regex3 = re.compile(r'<h2 class="film-name">.+?</h2>')
    titles = regex3.findall(movie_src)
    titles = [title.replace('<h2 class="film-name">', '').replace('</h2>', '') for title in titles]
    return titles

def get_user_choice_movie(titles):
    # get user choice
    user_movie_choice = input(f"\nChoose movie(1-{len(titles)}): ")
    return util.convert_to_int(user_movie_choice)

def display_titles(titles):
    for i, title in enumerate(titles):
        print(i + 1, title)

def get_movie_server_urls(movie_page_src, prefix):
    # get movie servers and links
    regex5 = re.compile(r'href="(.+?)"')
    regex6 = re.compile(r'/watch-movie/.+?')
    movie_servers = regex5.findall(movie_page_src)
    movie_servers = list(filter(regex6.search, movie_servers))
    movie_servers = list(dict.fromkeys(movie_servers))
    movie_servers = [prefix + link for link in movie_servers]
    movie_servers.pop(0)
    return movie_servers

def get_movie_server_names(movie_page_src):
    # get server names from span
    regex7 = re.compile(r'<span>.+?</span>')
    server_names = regex7.findall(movie_page_src)

    # refine server names ( there is only 3)
    server_names = [name.replace('<span>', '').replace('</span>', '') for name in server_names]
    server_names = server_names[2:5]
    print(server_names)
    return server_names

def get_user_server_choice(server_names):
    # get user choice
    user_server_choice = input(f"\nChoose server(1-{len(server_names)}): ")
    return util.convert_to_int(user_server_choice)

def loading_message():
    print("Loading Selections...\n")


def init_movie_protocol(prefix):
    # choose browser firefox or chrome
    print("Choose browser:\n1. Firefox\n2. Chrome")
    browser_choice = input("Enter choice: ")
    # if browser choice is firefox
    web_driver = emulation.validate_browser_choice(browser_choice)
    loading_message()

    genre_links = get_genres(web_driver)
    movie.display_genres_to_user(genre_links)

    user_choice = get_user_genre_choice(1, get_genre_count(genre_links))
    print('\n')

    movies, movie_src = user_choice_validator_loop(user_choice, genre_links, web_driver)
    titles = scrape_movie_titles(movie_src)
    user_movie_choice = get_user_choice_movie(titles)
    movie_url = prefix + movies[user_movie_choice - 1]
    movie_page_src = emulation.get_url_source(movie_url, web_driver)
    # movie_servers = get_movie_server_urls(movie_page_src, prefix)
    server_names = get_movie_server_names(movie_page_src)

    # close the driver on the user
    emulation.web_driver_soft_close(web_driver)
