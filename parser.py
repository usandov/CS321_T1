import requests

from bs4 import BeautifulSoup
from database import *


# https://stackoverflow.com/questions/41982475/scraper-in-python-gives-access-denied
def extract_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source = requests.get(url, headers=headers).text
    return source


buffalo_bills_roster_url = "https://www.espn.com/nfl/team/roster/_/name/buf/buffalo-bills"


page = extract_source(buffalo_bills_roster_url)

soup = BeautifulSoup(page, 'html.parser')

table_bodies = soup.select('.Table__TBODY')

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