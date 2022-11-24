mport urllib, re, os, subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

URL = "https://vipstream.tv/home"
urls = ('''https://vipstream.tv/genre/action
https://vipstream.tv/genre/action-adventure
https://vipstream.tv/genre/adventure
https://vipstream.tv/genre/animation
https://vipstream.tv/genre/biography
https://vipstream.tv/genre/comedy
https://vipstream.tv/genre/crime
https://vipstream.tv/genre/documentary
https://vipstream.tv/genre/drama
https://vipstream.tv/genre/family
https://vipstream.tv/genre/fantasy
https://vipstream.tv/genre/history
https://vipstream.tv/genre/horror
https://vipstream.tv/genre/kids
https://vipstream.tv/genre/music
https://vipstream.tv/genre/mystery
https://vipstream.tv/genre/news
https://vipstream.tv/genre/reality
https://vipstream.tv/genre/romance
https://vipstream.tv/genre/sci-fi-fantasy
https://vipstream.tv/genre/science-fiction
https://vipstream.tv/genre/soap
https://vipstream.tv/genre/talk
https://vipstream.tv/genre/thriller
https://vipstream.tv/genre/tv-movie
https://vipstream.tv/genre/war
https://vipstream.tv/genre/war-politics
https://vipstream.tv/genre/western
''')

genres = urls.replace("https://vipstream.tv/genre","")

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

# Create an object to hold list of genres and links

# 2d array of movie titles and links

# Finding the download link




def GetUrlSource(URL, driver):
    driver.get(URL)
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
                write_to_file(GetUrlSource(URL, driver))
                try:
                        driver.close()
                except:
                        pass

                print(links)

main()

#testing links change this later
def setupChrome():
        opts = ChromeOptions()
        driver2 = webdriver.Chrome(options=opts)
        Join = input('''Choose genre: ''')
        if Join.lower() == 'kids':
          driver2.get("https://vipstream.tv/genre/kids")
        elif Join.lower() == 'horror':
          driver2.get('https://vipstream.tv/genre/horror')
        elif Join.lower() == 'soap':
          driver2.get('https://vipstream.tv/genre/soap')
        else:
          print("Wrong Choice. Try Again")

setupChrome()








