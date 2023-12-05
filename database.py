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

def insertRoster_DB():
        connection = mysql.connector.connect(host=host, user=user, password=password , database="NFL_Teams")
        cursor = connection.cursor()

        roster = extract_RosterData(buffalo_bills_roster_url)

        for player in roster:
                query = "INSERT INTO NFL (Name, Position, Age, Height) VALUES (%s, %s, %s, %s)"
                var = (player[0], player[1], player[2], player[3])
                #print(player[0] + " " + player[1] + " " + player[2] + " " + player[3])
                cursor.execute(query, var)

        connection.commit()

        connection.close()

def main():

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
            Age VARCHAR(10),
            Height VARCHAR(25),
            PassingYards int, 
            PassingTDs int,
            TotalTackles int, 
            TotalSacks int, 
            Interceptions int, 
            FumblesRecovered int, 
            KicksBlocked int,
            FGMade int, 
            FGAttempted int, 
            EPRatio DECIMAL(3,3),
            Receptions int, 
            ReceivingYards int, 
            ReceivingTDs int 
        )
        """
        cursor.execute(create_table_query)
        connection.commit()

        insertRoster_DB()

        connection.close()


if __name__ == "__main__":
    main()


'''
https://stackoverflow.com/questions/6829675/the-proper-method-for-making-a-db-connection-available-across-many-python-module
'''

