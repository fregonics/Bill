import mysql.connector
import sqlConnection

ACCOUNT_INSERT_QUERY = 'insert into ACCOUNT(NAME, DESCRIPTION, INNERVALUE) values(%s, %s, %s)'
ACCOUNTS_LAST_ID_QUERY = 'select MAX(ID) from ACCOUNT'
ACCOUNT_SEARCH_WITH_ID_QUERY = 'select ID, NAME, DESCRIPTION, INNERVALUE from ACCOUNT where ID = %s'

class Account:

    def __init__(self, _name):
        self.name = _name
        self.value = 0
    
    #Set methods
    def setDescription(self, _description):
        self.description = _description
    
    def setValue(self, _value):
        self.value = _value
    
    #Get methods
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description

    def getValue(self):
        return self
    
    #Persistent storage methods
    def saveOnDatabase(self):
        db = sqlConnection.getConnection()
        cursor = db.cursor()
        
        account_data = (self.name, self.description, self.value)

        cursor.execute(ACCOUNT_INSERT_QUERY, account_data)
        db.commit()

        cursor.execute(ACCOUNTS_LAST_ID_QUERY)
        result = cursor.fetchall()
        
        cursor.close()
        db.close()

        for i in result:
            continue
      
        return i[0]

def getFromDatabase(accountId):
    db = sqlConnection.getConnection()
    cursor = db.cursor()
    data = (accountId,)
    
    cursor.execute(ACCOUNT_SEARCH_WITH_ID_QUERY, data)
    result = cursor.fetchall()
    
    cursor.close()
    db.close()
        
    i = result[0]

    account = Account(i[1])
    account.setDescription(i[2])
    account.setValue(i[3])
    return account