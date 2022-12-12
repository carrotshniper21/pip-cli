rom selenium import webdriver
from selenium.webdriver import ChromeOptions
import config

def validate_browser_choice(browser_choice):
    if browser_choice == "1" or browser_choice == "firefox":
        return setup_firefox()
        # if browser choice is chrome
    elif input == "2" or browser_choice == "chrome":
        return setup_chrome()
    else:
        print("Invalid choice, defaulting to Firefox")
        return setup_firefox()


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

def get_url_source(url, browser_headless):
    browser_headless.get(url)
    page_source = browser_headless.page_source
    return page_source
