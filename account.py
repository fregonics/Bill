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
        return self.value
    
