import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Zouhair12_MESTARI'
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE mycompany')