import mysql.connector

# connect server
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'rickyltwong',
    passwd = 'password'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE dundermifflin")

print("All Done!")