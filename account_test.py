import unittest
import account as ac

class AccountTest(unittest.TestCase):
    def test_create(self):
        acc = ac.Account("test")
        self.assertEqual(acc.getName(), "test", "Assert if account is correctly created and test is set")


if __name__ ==  '__main__' :
    unittest.main()

