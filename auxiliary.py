import requests
import json

# search int in string A and return founded int or default value B in case of exception
# usage: parse_number(string A, int B)
def parse_number(string, default_value):
    try:
        return int(string)
    except ValueError:
        return default_value

def unsplash_get_count(query):
    base = "https://unsplash.com/napi/search/photos"
    page = requests.get(f"{base}?query={query}&xp=&per_page=1&page=1&order_by=relevant")
    if page.ok:
        json_results = json.loads(page.text)
        return json_results['total']
    else:
        return 0

def unsplash_get_pic_url(query, page_n=1):
    base = "https://unsplash.com/napi/search/photos"
    page = requests.get(f"{base}?query={query}&xp=&per_page=1&page={page_n}&order_by=relevant")
    if page.ok:
        json_results = json.loads(page.text)
        return json_results['results'][0]['urls']['regular']
    else:
        return None
