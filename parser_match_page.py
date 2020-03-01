import requests
from bs4 import BeautifulSoup

URL = 'https://www.hltv.org/matches/2339860/hard-legion-vs-hellraisers-legendsbet-l33t-cup'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
            'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content_match_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='contentCol')

    list_match_info = []
    for item in items:
        list_match_info.append(
            {
                'bestof': item.find('div', class_='preformatted-text').get_text(),
                'name_team1': item.find('div', class_='map-stats-infobox').find_all('div', class_='team-name')[0].get_text(),
                'name_team2': item.find('div', class_='map-stats-infobox').find_all('div', class_='team-name')[1].get_text(),
                'maps_name1': item.find('div', class_='map-stats-infobox').find_all('div', class_='mapname')[0].get_text(),
                'maps_name2': item.find('div', class_='map-stats-infobox').find_all('div', class_='mapname')[1].get_text(),
                'maps_name3': item.find('div', class_='map-stats-infobox').find_all('div', class_='mapname')[2].get_text(),
                'maps_name4': item.find('div', class_='map-stats-infobox').find_all('div', class_='mapname')[3].get_text(),
                'maps_name5': item.find('div', class_='map-stats-infobox').find_all('div', class_='mapname')[4].get_text(),
                'maps_name6': item.find('div', class_='map-stats-infobox').find_all('div', class_='mapname')[5].get_text(),
                'maps_name7': item.find('div', class_='map-stats-infobox').find_all('div', class_='mapname')[6].get_text(),
                'map_stats1': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[0].get_text(),
                'map_stats2': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[1].get_text(),
                'map_stats3': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[2].get_text(),
                'map_stats4': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[3].get_text(),
                'map_stats5': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[4].get_text(),
                'map_stats6': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[5].get_text(),
                'map_stats7': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[6].get_text(),
                'map_stats8': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[7].get_text(),
                'map_stats9': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[8].get_text(),
                'map_stats10': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[9].get_text(),
                'map_stats11': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[10].get_text(),
                'map_stats12': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[11].get_text(),
                'map_stats13': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[12].get_text(),
                'map_stats14': item.find('div', class_='map-stats-infobox').find_all('a', class_='a-reset')[13].get_text(),
            }
        )
    return list_match_info

def print_info_match(info_matche):
    for obj_list in info_matche:
        print('____________________________________')
        print(obj_list['bestof'])
        print('Team1 - ' + obj_list['name_team1'])
        print('Team2 - ' + obj_list['name_team2'])
        print('******************************************')
        print(obj_list['maps_name1'] + '\t | \t' + obj_list['map_stats1' ]+ '\t | \t' + obj_list['map_stats2'] + '\t | ')
        print(obj_list['maps_name2'] + '\t | \t' + obj_list['map_stats3' ]+ '\t | \t' + obj_list['map_stats4'] + '\t | ')
        print(obj_list['maps_name3'] + '\t | \t' + obj_list['map_stats5' ]+ '\t | \t' + obj_list['map_stats6'] + '\t | ')
        print(obj_list['maps_name4'] + '\t | \t' + obj_list['map_stats7' ]+ '\t | \t' + obj_list['map_stats8'] + '\t | ')
        print(obj_list['maps_name5'] + '\t | \t' + obj_list['map_stats9' ]+ '\t | \t' + obj_list['map_stats10'] + '\t | ')
        print(obj_list['maps_name6'] + ' | \t' + obj_list['map_stats11' ]+ '\t | \t' + obj_list['map_stats12'] + '\t | ')
        print(obj_list['maps_name7'] + '\t | \t' + obj_list['map_stats13' ]+ '\t | \t' + obj_list['map_stats14'] + '\t | ')
        print('******************************************')
        #print(obj_list['map_stats'])
        #print('____________________________________')

    
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        match_info = get_content_match_info(html.text)
        print_info_match(match_info)
    else:
        print("error not 200")

parse()