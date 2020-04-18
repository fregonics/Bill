import transaction
import transaction_db

def findTransactionById(_id):
    data = transaction_db.read(_id)
    transaction_data = (data[1], data[2], data[4], data[5])
    tr = transaction.Transaction(transaction_data)
    tr.setId(data[0])
    return tr