import pypyodbc
import requests
from bs4 import BeautifulSoup

mySQLServer = ".\SQLEXPRESS"
myDatabase = "HLTV"

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 YaBrowser/20.2.3.213 Yowser/2.5 Safari/537.36',
            'accept': '*/*'}

connection = pypyodbc.connect("DRIVER={SQL Server};SERVER="+ mySQLServer +";DATABASE="+ myDatabase +";Trusted_Connection=true")

cursor = connection.cursor() # бегунок

mySQLQuery = ("""
                SELECT Team, Nickname, URL
                FROM dbo.Players
                WHERE Team = 'ШУЕ'
""")

cursor.execute(mySQLQuery)
results = cursor.fetchall()

def get_html(url, params=None): 
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='responsive_page_template_content')

    hours_played = ""
    for item in items:
        hours_played = item.find('div', class_='recentgame_recentplaytime')
        if hours_played:
            hours_played = item.find('div', class_='recentgame_recentplaytime').get_text(strip=True)
        else:
            hours_played = 'Скрыта'
    return hours_played

for row in results:
    player_team = row[0]
    player_nickname = row[1]
    player_url = row[2]
    
    URL = player_url

    if (URL != "NONE                                                                                                                                                                                                                                                            "):
        html = get_html(URL)
        if html.status_code == 200:
            player_activity = get_content(html.text)
        else:
            print("error not 200")
    else:
        player_activity = "Профиль игрока не найден!"
    
    print("\nКоманда: " + str(player_team) + "\nНикнейм: " + str(player_nickname) + "\nИгровая активность: " + str(player_activity))

connection.close()