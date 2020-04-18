import account as acc
import transaction_db

class Transaction:
    def __init__(self, data):
        self.id = None
        self.origin_acc_id = data[0]
        self.destiny_acc_id = data[1]
        self.description = data[2]
        self.value = data[3]
    
    # GET METHODS
    def getDescription(self):
        return self.description
    
    def getValue(self):
        return self.value

    def getOrigin(self):
        return acc.getFromDatabase(self.origin_acc_id)
    
    def getDestiny(self):
        return acc.getFromDatabase(self.destiny_acc_id)

    def getId(self):
        return self.id
    
    def isExecuted(self):
        return (not self.id == None)

    # SET METHODS
    def setDescription(self, _description):
        self.description = _description
    
    def setValue(self, _value):
        self.value = _value
    
    def setOrigin(self, _origin):
        self.origin_acc_id = _origin

    def setDestiny(self, _destiny):
        self.destiny_acc_id = _destiny
    
    def setId(self, _id):
        self.id = _id

    #PERSISTENT STORAGE
    def commit(self):
        self.id = transaction_db.write(self)
        return self.id