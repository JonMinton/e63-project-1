import unittest

# Add imports here
from models.transaction import Transaction
from models.account import Account
from models.customer import Customer
from models.merchant import Merchant
from models.bank import Bank

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.bnk = Bank("Banksy")
        self.cst = Customer("Jim", "Reed")
        self.act = Account(self.bnk, self.cst, 500.00)
        self.mch = Merchant("Shooie Jims")
        self.trns1 = Transaction(self.act, self.mch, 20.00)
        


    def test_transaction_has_expected_properties(self):
        self.assertEqual(
            "Reed",
            self.trns1.account.customer.last_name
        )
        self.assertEqual(
            "Shooie Jims",
            self.trns1.merchant.name
        )
        self.assertEqual(
            20.00,
            self.trns1.amount
        )

    def test_later_transaction_has_bigger_timestamp(self):
        new_trans = Transaction(self.act, self.mch, 50.00)
        self.assertTrue(
            new_trans.timestamp > self.trns1.timestamp
        )

