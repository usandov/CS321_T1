

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
	if "QB" in result
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
	assert result[0] = "Tim Boyle QB 29 6\' 4\""

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
