import requests
from bs4 import BeautifulSoup

arizona_cardinals = "https://www.espn.com/nfl/team/roster/_/name/ari/arizona-cardinals"
baltimore_ravens = "https://www.espn.com/nfl/team/roster/_/name/bal/baltimore-ravens"
atlanta_falcons = "https://www.espn.com/nfl/team/roster/_/name/atl/atlanta-falcons"
buffalo_bills_roster_url = "https://www.espn.com/nfl/team/roster/_/name/buf/buffalo-bills"
carolina_panthers = "https://www.espn.com/nfl/team/roster/_/name/car/carolina-panthers"
cincinnati_bengals = "https://www.espn.com/nfl/team/roster/_/name/cin/cincinnati-bengals"
chicago_bears = "https://www.espn.com/nfl/team/roster/_/name/chi/chicago-bears"
cleveland_browns = "https://www.espn.com/nfl/team/roster/_/name/cle/cleveland-browns"
dallas_cowboys = "https://www.espn.com/nfl/team/roster/_/name/dal/dallas-cowboys"
denver_broncos = "https://www.espn.com/nfl/team/roster/_/name/den/denver-broncos"
detriot_lions = "https://www.espn.com/nfl/team/roster/_/name/det/detroit-lions"
houston_texans = "https://www.espn.com/nfl/team/roster/_/name/hou/houston-texans"
greenbay_packers = "https://www.espn.com/nfl/team/roster/_/name/gb/green-bay-packers"
indianapolis_colts = "https://www.espn.com/nfl/team/roster/_/name/ind/indianapolis-colts"
la_rams = "https://www.espn.com/nfl/team/roster/_/name/lar/los-angeles-rams"
jacksonville_jaguars = "https://www.espn.com/nfl/team/roster/_/name/jax/jacksonville-jaguars"
minnisota_vikings = "https://www.espn.com/nfl/team/roster/_/name/min/minnesota-vikings"
kc_cheifs = "https://www.espn.com/nfl/team/roster/_/name/kc/kansas-city-chiefs"
no_saints = "https://www.espn.com/nfl/team/roster/_/name/no/new-orleans-saints"
lv_raiders = "https://www.espn.com/nfl/team/roster/_/name/lv/las-vegas-raiders"
ny_giants = "https://www.espn.com/nfl/team/roster/_/name/nyg/new-york-giants"
la_chargers = "https://www.espn.com/nfl/team/roster/_/name/lac/los-angeles-chargers"
philadelphia_eagles = "https://www.espn.com/nfl/team/roster/_/name/phi/philadelphia-eagles"
miami_dolphins = "https://www.espn.com/nfl/team/roster/_/name/mia/miami-dolphins"
sf_49ers = "https://www.espn.com/nfl/team/roster/_/name/sf/san-francisco-49ers"
ne_patriots = "https://www.espn.com/nfl/team/roster/_/name/ne/new-england-patriots"
seattle_seahawks = ""
ny_jets = ""
tb_buccaneers = ""
pittsburgh_steelers = ""
washington_commanders = ""
tennessee_titans = ""

def extract_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source = requests.get(url, headers=headers).text
    return source

    '''
        Returns multi dimensional array of strings with each element in following format:
        [{name}, {position}, {age}, {height}]
        Exmaple: 
        Josh Allen QB 27 6' 5"
        '''
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

    # for player in players_details:
    #     print(player[0] + " " + player[1] + " " + player[2] + " " + player[3])


    return players_details

# extract_RosterData(buffalo_bills_roster_url)