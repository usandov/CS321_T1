
#Testing File

from parser import *
from parser2 import *
from database import *


def test_first():
	mycursor.execute("SELECT Name FROM NFL")
	result = mycursor.fetchone()
	assert result == "Josh Allen"

def test_second():
	mycursor.execute("SELECT Name FROM NFL")
	result = mycursor.fetchall()
	assert result.index("Kyle Allen") == 1

def test_many():
	mycursor.execute("SELECT Name FROM NFL")
	result = mycursor.fetchall()
	assert result.index("Josh Allen") == 0 and result.index("Shane Beuchele") == 2

def test_position():
	mycursor.execute("SELECT Name, Position FROM NFL")
	result = mycursor.fetchone()
	if "QB" in result:
		assert True
	assert False

def test_QB():
	mycursor.execute("SELECT Name FROM NFL WHERE position ='QB'")
	result = mycursor.fetchall()
	assert result == ["Josh Allen", "Kyle Allen", "Shane Buechele"]
	
def test_defense():
	mycursor.execute("SELECT Name FROM NFL")
	result = mycursor.fetchall()
	assert result[35] == "Kameron Cline"
	
def test_specialTeams():
	mycursor.execute("SELECT Name FROM NFL")
	result = mycursor.fetchall()
	assert result[70] == "Tyler Bass"

def test_teamMIA():
	result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/mia/miami-dolphins")
	assert result[0] == "Tua Tagovailoa QB 25 6\' 1\""

def test_teamMIADef():
	result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/mia/miami-dolphins")
	assert result[40] == "Emmanuel Ogbah DE 29 6\' 4\""

def test_teamNE():
	result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/ne/new-england-patriots")
	assert result[0] == "Malik Cunningham QB 25 6\' 1\""

def test_teamNEDef():
	result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/ne/new-england-patriots")
	assert result[37] == "Trey Flowers DE 30 6\' 2\""

def test_teamNYJ():
	result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/nyj/new-york-jets")
	assert result[0] == "Tim Boyle QB 29 6\' 4\""

def test_teamNYJDef():
	result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/nyj/new-york-jets")
	assert result[37] == "Micheal Clemons DE 26 6\' 5\""

def test_teamBAL():
	result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/bal/baltimore-ravens")
	assert result[0] == "Tyler Huntley QB 25 6\' 1\""

def test_teamBALDef():
	result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/bal/baltimore-ravens")
	assert result[37] == "Brent Urban DE 32 6\' 7\""

def test_teamCIN():
	result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/cin/cincinnati-bengals")
	assert result[0] == "Jake Browning QB 27 6\' 2\""

def test_teamCINDef():
	result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/cin/cincinnati-bengals")
	assert result[34] == "Jeff Gunter DE 24 6\' 4\""

def test_playerOne():
	result = extract_PlayerStats("https://www.espn.com/nfl/player/stats/_/id/4379399/james-cook")
	assert result == ["James Cook", 507, 1, 21]
	
def test_playerTwo():
	result = extract_PlayerStats("https://www.espn.com/nfl/player/stats/_/id/3925347/damien-harris")
	assert result == ["Damien Harris", 462, 0, 17]

def test_playerThree():
	result = extract_PlayerStats("https://www.espn.com/nfl/player/stats/_/id/3915411/ty-johnson")
	assert result == ["Ty Johnson", 160, 2, 12]

def test_Josh():
	result = queryPlayer("Josh Allen")
	assert result == [762, 3, 0]

def test_Kyle():
	result = queryPlayer("Kyle Allen")
	assert result == [13, 0, 0]
	
def test_StatsArizona():
	url1 = 'https://www.espn.com/nfl/team/roster/_/name/ari/arizona-cardinals'
	url2 = 'https://www.espn.com/nfl/team/stats/_/name/ari/arizona-cardinals'
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Joshua Dobbs")
	assert result == [1569, 258]
	
def test_StatsRavens():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/bal/baltimore-ravens"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/bal/baltimore-ravens"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Lamar Jackson")
	assert result == [2618, 574]
	
def test_StatsFalcons():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/atl/atlanta-falcons"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/atl/atlanta-falcons"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Desmond Ridder")
	assert result == [2029, 180]
	
def test_StatsBills():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/buf/buffalo-bills"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/buf/buffalo-bills"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Josh Allen")
	assert result == [3214, 342]
	
def test_StatsPanthers():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/car/carolina-panthers"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/car/carolina-panthers"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Bryce Young")
	assert result == [2055, 161]
	
def test_StatsBengals():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/cin/cincinnati-bengals"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/cin/cincinnati-bengals"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Joe Burrow")
	assert result == [2309, 88]
	
def test_StatsBears():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/chi/chicago-bears"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/chi/chicago-bears"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Cade McNamara")
	assert result == [2576, 26]
	
def test_StatsBrowns():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/cle/cleveland-browns"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/cle/cleveland-browns"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Deshaun Watson")
	assert result == [1115, 142]

def test_StatsCowboys():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/dal/dallas-cowboys"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/dal/dallas-cowboys"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Dak Prescott")
	assert result == [3234, 174]

def test_StatsBroncos():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/den/denver-broncos"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/den/denver-broncos"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Russell Wilson")
	assert result == [2385, 310]
	
def test_StatsLions():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/det/detroit-lions"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/det/detroit-lions"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Jared Goff")
	assert result == [3288, 21]
	
def test_StatsTexans():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/hou/houston-texans"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/hou/houston-texans"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = C.J. Stroud")
	assert result == [3540, 143]
	
def test_StatsPackers():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/gb/green-bay-packers"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/gb/green-bay-packers"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Jordan Love")
	assert result == [2866, 231]
	
def test_StatsColts():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/ind/indianapolis-colts"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/ind/indianapolis-colts"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Gardener Minshew")
	assert result == [2284, 52]
	
def test_StatsRams():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/lar/los-angeles-rams"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/lar/los-angeles-rams"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Matthew Stafford")
	assert result == [2768, 69]
	
def test_StatsJaguars():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/jax/jacksonville-jaguars"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/jax/jacksonville-jaguars"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Trevor Lawrence")
	assert result == [3004, 248]
	
def test_StatsVikings():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/min/minnesota-vikings"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/min/minnesota-vikings"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Kirk Cousins")
	assert result == [2331, 25]
	
def test_StatsChiefs():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/kc/kansas-city-chiefs"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/kc/kansas-city-chiefs"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Patrick Mahomes")
	assert result == [3127, 331]
	
def test_StatsSaints():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/no/new-orleans-saints"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/no/new-orleans-saints"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Derek Carr")
	assert result == [2761, 39]
	
def test_StatsRaiders():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/lv/las-vegas-raiders"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/lv/las-vegas-raiders"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Jimmy Garoppolo")
	assert result == [1205, 39]
	
def test_StatsGiants():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/nyg/new-york-giants"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/nyg/new-york-giants"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Daniel Jones")
	assert result == [909, 206]
	
def test_StatsChargers():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/lac/los-angeles-chargers"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/lac/los-angeles-chargers"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Justin Herbert")
	assert result == [3038, 228]
	
def test_StatsEagles():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/phi/philadelphia-eagles"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/phi/philadelphia-eagles"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Jalen Hurts")
	assert result == [2995, 430]
	
def test_StatsDolphins():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/mia/miami-dolphins"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/mia/miami-dolphins"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Tua Tagovailoa")
	assert result == [3457, 40]
	
def test_Stats49ers():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/sf/san-francisco-49ers"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/sf/san-francisco-49ers"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Brock Purdy")
	assert result == [3185, 131]
	
def test_StatsPatriots():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/ne/new-england-patriots"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/ne/new-england-patriots"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Mac Jones")
	assert result == [2120, 96]
	
def test_StatsSeahawks():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/sea/seattle-seahawks"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/sea/seattle-seahawks"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Geno Smith")
	assert result == [2918, 92]
	
def test_StatsJets():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/nyj/new-york-jets"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/nyj/new-york-jets"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Zach Wilson")
	assert result == [1944, 199]
	
def test_StatsBuccaneers():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/tb/tampa-bay-buccaneers"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/tb/tampa-bay-buccaneers"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Baker Mayfield")
	assert result == [2790, 151]
	
def test_StatsSteelers():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/pit/pittsburgh-steelers"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/pit/pittsburgh-steelers"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Kenny Pickett")
	assert result == [2070, 54]
	
def test_StatsCommanders():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/wsh/washington-commanders"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/wsh/washington-commanders"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Sam Howell")
	assert result == [3466, 243]
	
def test_StatsTitans():
	url1 = "https://www.espn.com/nfl/team/roster/_/name/ten/tennessee-titans"
	url2 = "https://www.espn.com/nfl/team/stats/_/name/ten/tennessee-titans"
	insertRoster_DB(url1, url2)
	cursor = connection.cursor()
	result = cursor.execute("SELECT PassingYards, RushingYards FROM NFL WHERE Name = Will Levis")
	assert result == [1266, 17]

def test_database_integration():
    """
    
    test_database_integration() tests the integration of the database.py file with the parser.py file.

    Functions tested: insertRoster_DB(), main(), extract_RosterData()
    """

    # Create main table in the database by running the main function in database.py
    main()


    # Retrieve player names from the database

    connection = mysql.connector.connect(host=host, user=user, password=password , database="NFL_Teams")
    cursor = connection.cursor()
    cursor.execute("SELECT Name FROM NFL")
    retrieved_data = cursor.fetchall()
    connection.close()


    # Assert names are in the database

    #Buffalo Bills
    assert "Josh Allen" in retrieved_data
    assert "Kyle Allen" in retrieved_data
    assert "Shane Buechele" in retrieved_data
   
    #Arizona Cardinals
    assert "Kyler Murray" in retrieved_data
    assert "Jeff Driskel" in retrieved_data
    assert "Clayton Tune" in retrieved_data

    #Baltimore Ravens
    assert "Brent Urban" in retrieved_data
    assert "Travis Jones" in retrieved_data
    assert "Justin Madubuike" in retrieved_data

    #Atlanta Falcons
    assert "Ikenna Enechukwu" in retrieved_data
    assert "Joe Gaziano" in retrieved_data
    assert "Demone Harris" in retrieved_data




def test_parser_integration1():
    """

    test_parser_integration() tests the integration of the parser.py file methods

    """

    # Test the extract_RosterData() method which also runs the extract_source() method

    result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/buf/buffalo-bills")

    assert result is not None

    assert ['Josh Allen', 'QB', '27', '6\' 5"'] in result
    assert ['Kyle Allen', 'QB', '27', '6\' 3"'] in result
    assert ['Shane Buechele', 'QB', '25', '6\' 0"'] in result


def test_parser_integration2():
    """

    test_parser_integration() tests the integration of the parser.py file methods

    """

    # Test the extract_RosterData() method which also runs the extract_source() method

    result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/ari/arizona-cardinals")

    assert result is not None

    assert ['Kyler Murray', 'QB', '26', '5\' 10"'] in result
    assert ['Jeff Driskel', 'QB', '30', '6\' 4"'] in result
    assert ['Clayton Tune', 'QB', '24', '6\' 3"'] in result


def test_parser_integration3():
    """

    test_parser_integration() tests the integration of the parser.py file methods

    """

    # Test the extract_RosterData() method which also runs the extract_source() method

    result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/bal/baltimore-ravens")

    assert result is not None

    assert ['Brent Urban', 'DE', '32', '6\' 7"'] in result
    assert ['Travis Jones', 'DT', '24', '6\' 4"'] in result
    assert ['Justin Madubuike', 'DT', '26', '6\' 3"'] in result


def test_parser_integration4():
    """

    test_parser_integration() tests the integration of the parser.py file methods

    """

    # Test the extract_RosterData() method which also runs the extract_source() method

    result = extract_RosterData("https://www.espn.com/nfl/team/roster/_/name/atl/atlanta-falcons")

    assert result is not None

    assert ['Ikenna Enechukwu', 'DE', '23', '6\' 4"'] in result
    assert ['Joe Gaziano', 'DE', '27', '6\' 4"'] in result
    assert ['Demone Harris', 'DE', '27', '6\' 4"'] in result

def test_parser2_integration1():
    """

    test_parser2_integration() tests the integration of the parser2.py file methods

    """

    # Test the init() method which runs extract_positions() and scrape_table()

    result = init("https://www.espn.com/nfl/team/stats/_/name/buf/buffalo-bills")

    # Assert that the result is a list

    assert result is not None
    assert type(result) == list
    assert len(result) > 0

def test_parser2_integration2():
    """

    test_parser2_integration() tests the integration of the parser2.py file methods

    """

    # Test the init() method which runs extract_positions() and scrape_table()

    result = init("https://www.espn.com/nfl/team/stats/_/name/ari/arizona-cardinals")

    # Assert that the result is a list

    assert result is not None
    assert type(result) == list
    assert len(result) > 0

def test_parser2_integration3():
    """

    test_parser2_integration() tests the integration of the parser2.py file methods

    """

    # Test the init() method which runs extract_positions() and scrape_table()

    result = init("https://www.espn.com/nfl/team/stats/_/name/bal/baltimore-ravens")

    # Assert that the result is a list

    assert result is not None
    assert type(result) == list
    assert len(result) > 0    

def test_parser2_integration4():
    """

    test_parser2_integration() tests the integration of the parser2.py file methods

    """

    # Test the init() method which runs extract_positions() and scrape_table()

    result = init("https://www.espn.com/nfl/team/stats/_/name/atl/atlanta-falcons")

    # Assert that the result is a list

    assert result is not None
    assert type(result) == list
    assert len(result) > 0	