import mysql.connector
import sqlConnection
import datetime 

FIELDS = 'ORIGIN_ID, DESTINY_ID, MOMENT, DESCRIPTION, TRANSACTION_VALUE'

INSERT_QUERY = 'insert into TRANSACTION ('+FIELDS+') values(%s, %s, %s, %s, %s)'

def save(tr):
    db = sqlConnection.getConnection()
    cursor = db.cursor()
    data = (tr.origin_acc_id, tr.destiny_acc_id, datetime.datetime.now(), tr.description, tr.value)

    cursor.execute(INSERT_QUERY, data)
    db.commit()

    cursor.close()
    db.close()