import mysql.connector
import sqlConnection
import datetime 

FIELDS = 'ORIGIN_ID, DESTINY_ID, MOMENT, DESCRIPTION, TRANSACTION_VALUE'

INSERT_QUERY = 'insert into TRANSACTION ('+FIELDS+') values(%s, %s, %s, %s, %s)'
SELECT_ONE_QUERY = 'select ID, '+FIELDS+' from TRANSACTION where ID = %s'
SELECT_LAST_ID_QUERY = 'select MAX(ID) from TRANSACTION'

def write(tr):
    db = sqlConnection.getConnection()
    cursor = db.cursor()
    data = (tr.origin_acc_id, tr.destiny_acc_id, datetime.datetime.now(), tr.description, tr.value)

    cursor.execute(INSERT_QUERY, data)
    db.commit()

    cursor.close()
    db.close()

    return getLastId()

def read(_id):
    db = sqlConnection.getConnection()
    cursor = db.cursor()

    cursor.execute(SELECT_ONE_QUERY, (_id,))
    result = cursor.fetchAll()
    data = result[0]

    cursor.close()
    db.close()

    return data

def getLastId():
    db = sqlConnection.getConnection()
    cursor = db.cursor()

    cursor.execute(SELECT_LAST_ID_QUERY)

    cursor.close()
    db.close()
