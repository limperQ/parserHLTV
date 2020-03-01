import requests
from bs4 import BeautifulSoup

URL = 'https://www.hltv.org/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
            'accept': '*/*'}
HOST = 'https://www.hltv.org'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='hotmatch-box')

    list_hot_matches = []
    for item in items:
        list_hot_matches.append(
            {
                'team': item.find('div', class_='teamrows').get_text(),
                'title': item.get('title'),
                'url': HOST + item.get('href'),
                'stars': item.find('div', class_='teambox').get('stars'),
            }
        )
    return list_hot_matches

def print_matches(matches):
    for obj_list in matches:
        print('____________________________________')
        print('Teams: ' + obj_list['team'])
        print('Title: ' + obj_list['title'])
        print('URL: ' + obj_list['url'])
        print('Stars: ' + obj_list['stars'])
        #print('____________________________________')
    

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        matches = get_content(html.text)
        print_matches(matches)
    else:
        print("error not 200")

parse()