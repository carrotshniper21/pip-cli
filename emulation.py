from selenium import webdriver
from selenium.webdriver import ChromeOptions
import config


def setup_firefox():
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver_f = webdriver.Firefox(options=options)
    driver_f.get(config.BASE_URL)
    return driver_f


def setup_chrome():
    opts = ChromeOptions()
    opts.headless = True
    chrome_headless = webdriver.Chrome(options=opts)
    return chrome_headless


def web_driver_soft_close(web_driver):
    try:
        web_driver.close()
    except:
        pass
