

def test_first():
	mycursor.execute("SELECT Name FROM NFL")
	result = mycursor.fetchone()
	assert result = "Josh Allen"

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
	assert result = ["Josh Allen", "Kyle Allen", "Shane Buechele"]
	
def test_defense():
	mycursor.execute("SELECT Name FROM NFL")
	result = mycursor.fetchall()
	assert result[35] == "Kameron Cline"
	
def test_specialTeams():
	mycursor.execute("SELECT Name FROM NFL")
	result = mycursor.fetchall()
	assert result[70] == "Tyler Bass"

	