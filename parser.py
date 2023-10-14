import requests
from bs4 import BeautifulSoup

buffalo_bills_roster_url = "https://www.espn.com/nfl/team/roster/_/name/buf/buffalo-bills"

def extract_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source = requests.get(url, headers=headers).text
    return source


def extract_RosterData(url):
    page = extract_source(buffalo_bills_roster_url)
    soup = BeautifulSoup(page, 'html.parser')

    table_bodies = soup.select('.Table__TBODY')

    players_details = []

    for b in table_bodies:
        rows = b.select(".Table__TR.Table__TR--lg.Table__even")
        for row in rows:
            columns = row.select(".Table__TD")
            rawName = columns[1].text
            name = "".join([c for c in rawName if not c.isdigit()])
            position = columns[2].text
            age = columns[3].text
            height = columns[4].text

            # Store the details in the list
            players_details.append([name, position, age, height])


    return players_details
    '''
    Returns multi dimensional array of strings with each element in following format:
    [{name}, {position}, {age}, {height}]
    Exmaple: 
    Josh Allen QB 27 6' 5"
    '''