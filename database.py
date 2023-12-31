from getpass import getpass

import mysql
from mysql.connector import connect, Error
from parser import *
from parser2 import *

connection = None
host = "localhost"
user = "root"
password = getpass("Enter Password: ")
cursor = None

nfl_teams = [
        ["https://www.espn.com/nfl/team/roster/_/name/ari/arizona-cardinals","https://www.espn.com/nfl/team/stats/_/name/ari/arizona-cardinals"], #0arizona_cardinals
        ["https://www.espn.com/nfl/team/roster/_/name/bal/baltimore-ravens","https://www.espn.com/nfl/team/stats/_/name/bal/baltimore-ravens"], #1baltimore_ravens
        ["https://www.espn.com/nfl/team/roster/_/name/atl/atlanta-falcons","https://www.espn.com/nfl/team/stats/_/name/atl/atlanta-falcons"], #2atlanta_falcons
        ["https://www.espn.com/nfl/team/roster/_/name/buf/buffalo-bills","https://www.espn.com/nfl/team/stats/_/name/buf/buffalo-bills"], #3buffalo_bills
        ["https://www.espn.com/nfl/team/roster/_/name/car/carolina-panthers","https://www.espn.com/nfl/team/stats/_/name/car/carolina-panthers"], #4carolina_panthers
        ["https://www.espn.com/nfl/team/roster/_/name/cin/cincinnati-bengals", "https://www.espn.com/nfl/team/stats/_/name/cin/cincinnati-bengals"], #5cincinnati_bengals
        ["https://www.espn.com/nfl/team/roster/_/name/chi/chicago-bears", "https://www.espn.com/nfl/team/stats/_/name/chi/chicago-bears"], #6chicago_bears
        ["https://www.espn.com/nfl/team/roster/_/name/cle/cleveland-browns", "https://www.espn.com/nfl/team/stats/_/name/cle/cleveland-browns"], #7cleveland_browns
        ["https://www.espn.com/nfl/team/roster/_/name/dal/dallas-cowboys", "https://www.espn.com/nfl/team/stats/_/name/dal/dallas-cowboys"], #8dallas_cowboys
        ["https://www.espn.com/nfl/team/roster/_/name/den/denver-broncos","https://www.espn.com/nfl/team/stats/_/name/den/denver-broncos"], #9denver_broncos
        ["https://www.espn.com/nfl/team/roster/_/name/det/detroit-lions","https://www.espn.com/nfl/team/stats/_/name/det/detroit-lions"], #10detriot_lions
        ["https://www.espn.com/nfl/team/roster/_/name/hou/houston-texans","https://www.espn.com/nfl/team/stats/_/name/hou/houston-texans"], #11houston_texans
        ["https://www.espn.com/nfl/team/roster/_/name/gb/green-bay-packers" , "https://www.espn.com/nfl/team/stats/_/name/gb/green-bay-packers"], #12greenbay_packers
        ["https://www.espn.com/nfl/team/roster/_/name/ind/indianapolis-colts", "https://www.espn.com/nfl/team/stats/_/name/ind/indianapolis-colts"], #13indianapolis_colts
        ["https://www.espn.com/nfl/team/roster/_/name/lar/los-angeles-rams", "https://www.espn.com/nfl/team/stats/_/name/lar/los-angeles-rams"], #14la_rams
        ["https://www.espn.com/nfl/team/roster/_/name/jax/jacksonville-jaguars", "https://www.espn.com/nfl/team/stats/_/name/jax/jacksonville-jaguars"], #15jacksonville_jaguars
        ["https://www.espn.com/nfl/team/roster/_/name/min/minnesota-vikings", "https://www.espn.com/nfl/team/stats/_/name/min/minnesota-vikings"], #16minnisota_vikings
        ["https://www.espn.com/nfl/team/roster/_/name/kc/kansas-city-chiefs", "https://www.espn.com/nfl/team/stats/_/name/kc/kansas-city-chiefs"], #17kc_cheifs
        ["https://www.espn.com/nfl/team/roster/_/name/no/new-orleans-saints", "https://www.espn.com/nfl/team/stats/_/name/no/new-orleans-saints"], #18no_saints
        ["https://www.espn.com/nfl/team/roster/_/name/lv/las-vegas-raiders", "https://www.espn.com/nfl/team/stats/_/name/lv/las-vegas-raiders"], #19lv_raiders
        ["https://www.espn.com/nfl/team/roster/_/name/nyg/new-york-giants", "https://www.espn.com/nfl/team/stats/_/name/nyg/new-york-giants"], #20ny_giants
        ["https://www.espn.com/nfl/team/roster/_/name/lac/los-angeles-chargers", "https://www.espn.com/nfl/team/stats/_/name/lac/los-angeles-chargers"], #21la_charger
        ["https://www.espn.com/nfl/team/roster/_/name/phi/philadelphia-eagles", "https://www.espn.com/nfl/team/stats/_/name/phi/philadelphia-eagles"], #22philadelphia_eagles
        ["https://www.espn.com/nfl/team/roster/_/name/mia/miami-dolphins", "https://www.espn.com/nfl/team/stats/_/name/mia/miami-dolphins"], #23miami_dolphins
        ["https://www.espn.com/nfl/team/roster/_/name/sf/san-francisco-49ers", "https://www.espn.com/nfl/team/stats/_/name/sf/san-francisco-49ers"], #24sf_49ers
        ["https://www.espn.com/nfl/team/roster/_/name/ne/new-england-patriots", "https://www.espn.com/nfl/team/stats/_/name/ne/new-england-patriots"], #25ne_patriots
        ["https://www.espn.com/nfl/team/roster/_/name/sea/seattle-seahawks", "https://www.espn.com/nfl/team/stats/_/name/sea/seattle-seahawks"], #26seattle_seahawks
        ["https://www.espn.com/nfl/team/roster/_/name/nyj/new-york-jets", "https://www.espn.com/nfl/team/stats/_/name/nyj/new-york-jets"], #27ny_jets
        ["https://www.espn.com/nfl/team/roster/_/name/tb/tampa-bay-buccaneers", "https://www.espn.com/nfl/team/stats/_/name/tb/tampa-bay-buccaneers"], #28tb_buccaneers
        ["https://www.espn.com/nfl/team/roster/_/name/pit/pittsburgh-steelers", "https://www.espn.com/nfl/team/stats/_/name/pit/pittsburgh-steelers"], #29pittsburgh_steelers
        ["https://www.espn.com/nfl/team/roster/_/name/wsh/washington-commanders", "https://www.espn.com/nfl/team/stats/_/name/wsh/washington-commanders"], #30washington_commanders
        ["https://www.espn.com/nfl/team/roster/_/name/ten/tennessee-titans", "https://www.espn.com/nfl/team/stats/_/name/ten/tennessee-titans"] #31tennessee_titans
]
def insertRoster_DB(url1, url2):
        connection = mysql.connector.connect(host=host, user=user, password=password , database="NFL_Teams")
        cursor = connection.cursor()

        roster = extract_RosterData(url1)
        stats = init(url2)

        for player in roster:
                query = "INSERT INTO NFL (Name, Position, Age, Height) VALUES (%s, %s, %s, %s)"
                var = (player[0], player[1], player[2], player[3])
                #print(player[0] + " " + player[1] + " " + player[2] + " " + player[3])
                cursor.execute(query, var)

        connection.commit()

        for idx, table_data in enumerate(stats):
            query_string = ""
            for data in table_data:
                    if data[0] == 'Name':
                            continue
                    if data[0] == 'Total':
                            continue
                    if idx == 0:
                            yds = data[1]
                            query_string = """UPDATE NFL SET PassingYards = {yds}, PassingTDs = {tds} WHERE Name = "{name}"; """.format(yds = yds.replace(",", ""), tds = data[2], name = data[0])
                    if idx == 1:
                            yds = data[1]
                            query_string = """UPDATE NFL Set RushingYards = {yds}, RushingTDs = {tds} Where Name = "{name}";""".format(yds= yds.replace(",", ""), tds=data[2], name=data[0])
                    if idx == 2:
                            yds = data[2]
                            query_string = """
                                    UPDATE NFL 
                                    Set Receptions = {rcp}, ReceivingYards = {yds}, ReceivingTDs = {tds}
                                    Where Name = "{name}";""".format(rcp = data[1], yds= yds.replace(",",""), tds=data[3], name= data[0])
                    if idx == 3:
                            query_string = """
                                    UPDATE NFL 
                                    Set TotalTackles = {tot}, TotalSacks = {sacks}, Interceptions = {inte}, FumblesRecovered = {fum}, KicksBlocked = {blocked}
                                    Where Name = "{name}";""".format(tot=data[1],sacks=data[2],inte=data[3],fum = data[4], blocked = data[5],name=data[0])
                    if idx == 4:
                            query_string = """
                                    UPDATE NFL 
                                    Set FGMade = {fg}, FGAttempted = {fga}, EPRatio = {rat}
                                    Where Name = "{name}";""".format(fg=data[1], fga=data[2], rat = float(data[3]) ,name=data[0])
                    cursor.execute(query_string)
                    connection.commit()

        connection.commit()

        connection.close()

def main():

        connection = mysql.connector.connect(host=host,user=user,password=password)
        create_db_query = "CREATE DATABASE IF NOT EXISTS NFL_Teams"
        cursor = connection.cursor()
        cursor.execute(create_db_query)
        select_db_query = "USE NFL_Teams"
        cursor.execute(select_db_query)
        cursor.execute("SET SQL_SAFE_UPDATES = 0;")

        create_table_query = """
        CREATE TABLE IF NOT EXISTS NFL(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(100),
            Position VARCHAR(5),
            Age VARCHAR(10),
            Height VARCHAR(25),
            PassingYards int, 
            PassingTDs int,
            RushingYards int,
            RushingTDs int,
            Receptions int, 
            ReceivingYards int, 
            ReceivingTDs int,
            TotalTackles int, 
            TotalSacks int, 
            Interceptions int, 
            FumblesRecovered int, 
            KicksBlocked int,
            FGMade int, 
            FGAttempted int, 
            EPRatio double 
        )
        """
        cursor.execute(create_table_query)
        connection.commit()

        for team in nfl_teams:
                insertRoster_DB(team[0], team[1])
        #insertRoster_DB(nfl_teams[19][0],nfl_teams[19][1])

        connection.close()


if __name__ == "__main__":
    main()


'''
https://stackoverflow.com/questions/6829675/the-proper-method-for-making-a-db-connection-available-across-many-python-module
'''

