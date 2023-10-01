from getpass import getpass

import mysql
from mysql.connector import connect, Error

import requests

from bs4 import BeautifulSoup

connection = None
host = "localhost"
user = "root"
password = getpass("Enter Password: ")
cursor = None

try:
        connection = mysql.connector.connect(host=host,user=user,password=password)
        create_db_query = "CREATE DATABASE IF NOT EXISTS NFL_Teams"
        cursor = connection.cursor()
        cursor.execute(create_db_query)
        select_db_query = "USE NFL_Teams"
        cursor.execute(select_db_query)
        create_table_query = """
        CREATE TABLE IF NOT EXISTS NFL(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(100),
            Position VARCHAR(5),
            Age INT,
            Height VARCHAR(25)
        )"""

        cursor.execute(create_table_query)
        connection.commit()

except Error as e:
    print(e)



# https://stackoverflow.com/questions/41982475/scraper-in-python-gives-access-denied
def extract_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source = requests.get(url, headers=headers).text
    return source


buffalo_bills_roster_url = "https://www.espn.com/nfl/team/roster/_/name/buf/buffalo-bills"


page = extract_source(buffalo_bills_roster_url)

soup = BeautifulSoup(page, 'html.parser')

table_bodies = soup.select('.Table__TBODY')

connection = mysql.connector.connect(host=host,user=user,password=password, database = "NFL_Teams")
select_db_query = "USE NFL_Teams"
cursor = connection.cursor()
cursor.execute(select_db_query)
connection.commit()

for b in table_bodies:
    rows = b.select(".Table__TR.Table__TR--lg.Table__even")
    for row in rows:
        columns = row.select(".Table__TD")
        rawName = columns[1].text
        name = ""
        for c in rawName:
            if c.isdigit():
                continue
            name += c

        position = columns[2].text
        age = columns[3].text
        height = columns[4].text

        print(f"{name} {position} {age} {height}")

        query = "INSERT INTO NFL (Name, Position, Age, Height) VALUES (%s, %s, %s, %s)"
        var = (name, position, age, height)

        cursor.execute(query, var)

connection.commit()


connection.close()