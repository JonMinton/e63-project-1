import unittest

# Add imports here
from models.bank import Bank
from models.account import Account
from models.customer import Customer
from models.merchant import Merchant
from models.transaction import Transaction

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.cst1 = Customer("Jon", "Minton")
        self.cst2 = Customer("Mon", "Jinton")
        self.bnk  = Bank("Bank of River")
        self.cst2.open_account(self.bnk, 1000.99)


    def test_customer_has_name(self):
        self.assertEqual("Jon", self.cst1.first_name)
        self.assertEqual("Minton", self.cst1.last_name)
        self.assertEqual("Mon", self.cst2.first_name)
        self.assertEqual("Jinton", self.cst2.last_name)

    def test_customer_initially_has_none_id(self):
        self.assertEqual(None, self.cst1.id)
        self.assertEqual(None, self.cst2.id)

    def test_customer1_initially_has_no_accounts(self):
        self.assertEqual(0, len(self.cst1.accounts))
    
    def test_customer2_initially_has_one_account(self):
        self.assertEqual(1, len(self.cst2.accounts))


    def test_customer_can_open_account(self):
        my_bank = Bank("Noonoo")
        self.assertEqual(0, len(self.cst1.accounts))
        self.cst1.open_account(my_bank)
        self.assertEqual(1, len(self.cst1.accounts))

    def test_customer_can_open_account_with_initial_balance(self):
        my_bank = Bank("Noonoo")
        self.assertEqual(0, len(self.cst1.accounts))
        self.cst1.open_account(my_bank, 502.09)
        self.assertEqual(1, len(self.cst1.accounts))
        self.assertEqual(502.09, self.cst1.accounts[0].balance)

    def test_customer_can_buy_something(self):
        customer_account = self.cst2.accounts[0]
        self.assertEqual(1000.99, customer_account.balance)
        merc1 = Merchant("Cheapies")
        self.assertEqual(0.00, merc1.revenue)
        self.assertEqual(0, merc1.num_sales)
        self.assertEqual(0, len(customer_account.transactions))
        self.cst2.buy(customer_account, merc1, 0.99)
        self.assertEqual(1000.00, customer_account.balance)
        self.assertEqual(0.99, merc1.revenue)
        self.assertEqual(1, merc1.num_sales)
        self.assertEqual(1, len(customer_account.transactions))

    def test_customer_cannot_buy_something_they_cannot_afford(self):
        customer_account = self.cst2.accounts[0]
        self.assertEqual(1000.99, customer_account.balance)
        merc1 = Merchant("Price Touters")
        self.assertEqual(0.00, merc1.revenue)
        self.assertEqual(0, merc1.num_sales)
        self.assertEqual(0, len(customer_account.transactions))
        self.cst2.buy(customer_account, merc1, 1999.99)
        self.assertEqual(1000.99, customer_account.balance)
        self.assertEqual(0.0, merc1.revenue)
        self.assertEqual(0, merc1.num_sales)
        self.assertEqual(0, len(customer_account.transactions))


