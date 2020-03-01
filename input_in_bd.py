import pymysql.cursors
 
id_team = 0
id_nicname = 1
id_url = 2
d = 0

# Подключиться к базе данных.
connection = pymysql.connect(host='sql2.freesqldatabase.com',
                             user='sql2325074',
                             password='lR9%rC8!',                             
                             db='sql2325074',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")

strSteamProfiles = []
f = open('HLTV/STEAM.txt', 'r')
for line in f.readlines():
    strSteamProfiles += line

data = []
with open('HLTV/STEAM.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.split()
        for item in parts:
            data.append(item)
             
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `players` (`team`, `nickname`, `url`) VALUES (%s, %s, %s)"
        while d < (len(data)):
            cursor.execute(sql, (data[id_team], data[id_nicname], data[id_url]))
            id_team += 3
            id_nicname += 3
            id_url += 3
            d += 3

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `players`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()