from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE IF NOT EXISTS NFL_Teams"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
        select_db_query = "USE NFL_Teams"
        with connection.cursor() as cursor:
            cursor.execute(select_db_query)
        create_table_query = """
        CREATE TABLE IF NOT EXISTS NFL(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(100),
            Position VARCHAR(5),
            Age INT,
            Height INT
        )"""
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()
except Error as e:
    print(e)

