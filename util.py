import urllib

def internet_working():
    try:
        urllib.request.urlopen('https://google.com', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False

def convert_to_int(user_choice):
    return int(user_choice)