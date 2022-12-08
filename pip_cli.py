#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import time
import logo
import emulation
import movie
import util


def loading_message():
	print("Loading Selections...\n")


def main():
	print(logo.display_message())
	prefix = "https://vipstream.tv"

	if util.internet_working():
		# choose browser firefox or chrome
		print("Choose browser:\n1. Firefox\n2. Chrome")
		browser_choice = input("Enter choice: ")
		# if browser choice is firefox
		if browser_choice == "1" or browser_choice == "firefox":
			web_driver = emulation.setup_firefox()
		# if browser choice is chrome
		elif input == "2" or browser_choice == "chrome":
			time.sleep(3)
			web_driver = emulation.setup_chrome()
		else:
			print("Invalid choice, defaulting to Firefox")
			web_driver = emulation.setup_firefox()
		loading_message()

		genre_links = movie.get_genres(web_driver)
		movie.display_genres_to_user(genre_links)

		user_choice = movie.get_user_genre_choice(1, movie.get_genre_count(genre_links))
		print('\n')

		# loop until user enters valid choice
		while not movie.validate_user_genre_choice(user_choice, genre_links):
			print("Invalid choice, try again")
			user_choice = movie.get_user_genre_choice(1, movie.get_genre_count(genre_links))
		user_choice = util.convert_to_int(user_choice)

		movie_src = movie.get_movie_src(genre_links, user_choice, web_driver)
		movies = movie.get_movies_from_genre(movie_src)

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
		user_movie_choice = util.convert_to_int(user_movie_choice)
		print("Loading Titles...")
		print(titles)
		print(movies)

		movie_url = prefix + movies[user_movie_choice - 1]
		movie_page_src = movie.get_url_source(movie_url, web_driver)

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

		# refine server names ( there is only 3)
		server_names = [name.replace('<span>', '').replace('</span>', '') for name in server_names]
		server_names = server_names[2:5]
		print(server_names)

		server_choice = input(f"\nChoose server(1-{len(server_names)}): ")
		print("You have chosen dis server bro")
		server_choice = util.convert_to_int(server_choice)
		print(server_names[server_choice - 1])

		# server_page_src = get_url_source(server_url, web_driver)
		# save server page source to file
		# write_to_file(server_page_src)

		print("finding video... Not... lol")

		# close the driver on the user
		emulation.web_driver_soft_close(web_driver)


if __name__ == '__main__':
	main()
