import unittest

# Add imports here
from models.merchant import Merchant
from models.bank import Bank
from models.customer import Customer
from models.account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.bnk1 = Bank("Blood Bank")
        self.cst1 = Customer("Mon", "Jinton")
        self.acnt = Account(self.bnk1, self.cst1)


    def test_account_can_be_made(self):
        self.assertEqual("Blood Bank", self.acnt.bank.name)
        self.assertEqual("Jinton", self.acnt.customer.last_name)

    
    def test_balance_initially_zero_by_default(self):
        self.assertEqual(0.0, self.acnt.return_balance())

    def test_monies_can_be_deposited(self):
        self.assertEqual(0.0, self.acnt.return_balance())
        self.acnt.deposit_monies(35.50)
        self.assertEqual(35.50, self.acnt.return_balance())

    def test_accounts_initially_have_none_for_id(self):
        self.assertEqual(None, self.acnt.id)

    def test_account_inherits_bank_tags(self):
        self.assertEqual(0, len(self.acnt.tags))
        bnk2 = Bank("Tagbank")
        mct1 = Merchant("Stinky Sally's")
        bnk2.tag_merchant("Perfume", mct1)
        new_account = Account(bnk2, self.cst1)
        self.assertEqual(1, len(new_account.tags))
        self.assertEqual("Perfume", new_account.tags[0].name)
