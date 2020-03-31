import mysql.connector

def getConnection():
    db = mysql.connector.connect(
        host = "localhost",
        database = "BILL_TEST",
        user = "root",
        passwd = "howsoonisnow"
    )
    return db