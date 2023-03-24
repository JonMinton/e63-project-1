from models.account import Account
from models.bank import Bank
from models.merchant import Merchant

class Customer:
    def __init__(self, first_name, last_name, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = []
        self.id = id

    def open_account(self, bank, balance = 0.0):
        new_account = Account(bank, self, balance)
        self.accounts.append(new_account)

    def buy(self, account, merchant, amt):
        # n.b. change this to invoking a transaction object
        if account in self.accounts:
            if amt < account.balance:
                merchant.revenue += amt
                merchant.num_sales += 1
                account.make_transaction(merchant, amt)
