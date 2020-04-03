import unittest
import account as ac
import mysql.connector

class AccountTest(unittest.TestCase):
    def test_create(self):
        acc = ac.Account("test")
        self.assertEqual(acc.getName(), "test", "Assert if account is correctly created and test is set")

    def test_write(self):
        acc = ac.Account("test")
        acc.setValue(25)
        acc.setDescription("This is a test account")
        accId = acc.saveOnDatabase()

        ac2 = ac.getFromDatabase(accId)
        self.assertEqual(str(ac2.getName()) + "-" + str(ac2.getDescription()), "test-This is a test account",
                "Assert if the creation and deletion on database works")            


if __name__ ==  '__main__' :
    unittest.main()

