from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="NFL_Teams",
    ) as connection:
        # create_db_query = "CREATE DATABASE NFL_Teams"
        # with connection.cursor() as cursor:
        #     cursor.execute(create_db_query)
        create_db_query2 = """
        CREATE TABLE NFL(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(100),
            Position VARCHAR(5),
            Age INT,
            Height INT
        )"""
        with connection.cursor() as cursor:
            cursor.execute(create_db_query2)
            connection.commit()
except Error as e:
    print(e)

