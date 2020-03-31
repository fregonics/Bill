import mysql.connector
import sqlConnection

ACCOUNT_INSERT_QUERY = 'insert into ACCOUNT(NAME, DESCRIPTION, INNERVALUE) values(%s, %s, %s)'
ACCOUNT_LAST_QUERY = 'select MAX(ID) ID from ACCOUNT'

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

        cursor.execute(ACCOUNT_LAST_QUERY)
        result = cursor.fetchall()
        _id = int(result[0][0])
        
        cursor.close()
        db.close()

        return _id