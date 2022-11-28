import pytermgui as ptg
import re
import time
import urllib

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

BASE_URL = "https://vipstream.tv/home"

def setup_firefox():
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver_f = webdriver.Firefox(options=options)
    driver_f.get(BASE_URL)
    return driver_f

def get_genres(web_driver):
    elems = web_driver.find_elements(By.XPATH, "//a[@href]")
    links = []
    for elem in elems:
        link = elem.get_attribute('href')
        if 'genre' in elem.get_attribute('href'):
            return links


CONFIG = """
config:
    Label:
        styles:
            value: dim bold
    
    Window:
        styles:
            border: '60'
            corner: '60'
    
    Container:
        styles:
            border: '96'
            corner: '96'
"""

with ptg.YamlLoader() as loader:
    loader.load(CONFIG)

with ptg.WindowManager() as manager:
    window = (
        ptg.Window(
            "",
            ptg.Container(
		"""[33 bold]
    ____  ________        ________    ____
   / __ \/  _/ __ \      / ____/ /   /  _/
  / /_/ // // /_/ /_____/ /   / /    / /  
 / ____// // ____/_____/ /___/ /____/ /   
/_/   /___/_/          \____/_____/___/   
               """,
            ),
            ptg.Container(
        f"[33 bold]  "
            ),
            "",
            ["Submit", lambda *_: submit(manager, window)],
            width=60,
        )
        .center()
    )

    manager.add(window)
