import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host= "localhost",
        user="root",
        passwd="31081994",
        database="master_python",
        port=3306
    )
    cursor = database.cursor()
    return [database, cursor]