import urllib

def internet_working():
    try:
        urllib.request.urlopen('https://google.com', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False


def convert_to_int(user_choice):
    return int(user_choice)


def write_to_file(page_source):
    with open('page_source.html', 'w') as f:
        f.write(page_source)


def slice_dict(dict):
    return {k: dict[k] for k in dict.keys()}
