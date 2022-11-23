#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "https://vipstream.tv/home"


def SetupFirefox():
	options = webdriver.FirefoxOptions()
	options.headless = True

	driver = webdriver.Firefox(options=options)
	driver.get(URL)
	return driver


def GetGenres(driver):
	elems = driver.find_elements(By.XPATH, "//a[@href]")
	links = []
	for elem in elems:
		link = elem.get_attribute('href')
		if 'genre' in elem.get_attribute('href'):
			links.append(link)
	return links



# create an object to hold list of genres and links

# 2d array of movie titles and links

# finding the download link




def GetUrlSource(url, driver):
	driver.get(url)
	page_source = driver.page_source
	driver.close()
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


def main():
	if internet_working():
		driver = SetupFirefox()
		links = GetGenres(driver)
	#write_to_file(GetUrlSource(URL, driver))
		try:
			driver.close()
		except:
			pass

		print(links)

main()
