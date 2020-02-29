import requests
from bs4 import BeautifulSoup


URL = 'https://www.hltv.org/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
            'accept': '*/*'}

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
                'url': 'https://www.hltv.org' + item.get('href')
            }
        )

    for obj_list in list_hot_matches:
        print(obj_list)
        print('\n')
    print(len(list_hot_matches))

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("error not 200")

parse()