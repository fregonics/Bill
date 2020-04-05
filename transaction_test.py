import unittest
import transaction as tr
import transaction_utils
import mysql.connector

class TransactionTest(unittest.TestCase):
    def test_make_transaction(self):
        t1 = tr.Transaction((1,2,'this is a test transaction', 12.5))
        _id = t1.commit()

        t2 = transaction_utils.findTransactionById(_id)
        self.assertEqual(t1.description, t2.description, 'Assert read and write operations for transactions')

if __name__ == '__main__':
    unittest.main()
