import requests
import wget
import zipfile
import os
import sys

url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
response = requests.get(url)
version_number = response.text

def define_download(version_number):
    
    if sys.platform.startswith("linux"):
        download_url = "https://chromedriver.storage.googleapis.com/" + version_number + "/chromedriver_linux64.zip"
    elif sys.platform.startswith("darwin"):
        download_url = "https://chromedriver.storage.googleapis.com/" + version_number + "/chromedriver_mac64.zip"
    elif sys.platform.startswith("win32"):
        download_url = "https://chromedriver.storage.googleapis.com/" + version_number + "/chromedriver_win32.zip"

    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall()

    os.remove(latest_driver_zip)

define_download(version_number)

#import requests
#import wget
#import zipfile
#import os
#import sys

#url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
#response = requests.get(url)
#version_number = response.text

#def define_download(version_number):
#    download_url = "https://chromedriver.storage.googleapis.com/{}/chromedriver_{}64.zip".format(version_number, sys.platform)
#    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

#    zipfile.ZipFile(latest_driver_zip).extractall()
#    os.remove(latest_driver_zip)

#define_download(version_number)
