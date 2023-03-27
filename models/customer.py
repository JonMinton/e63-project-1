from models.account import Account
from models.merchant import Merchant
from models.tag import Tag

class Customer:
    def __init__(self, first_name, last_name, budget = 0.0, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.budget = budget
        self.id = id

    # def open_account(self, bank, balance = 0.0):
    #     new_account = Account(bank, balance)
    #     self.accounts.append(new_account)

    # def buy(self, account, merchant, amt):
    #     # n.b. change this to invoking a transaction object
    #     if account in self.accounts:
    #         if amt < account.balance:
    #             merchant.revenue += amt
    #             merchant.num_sales += 1
    #             account.make_transaction(merchant, amt)

    # def tag_merchant(self, tagname, merchant):

    #     if len(self.accounts) > 0:
    #         for account in self.accounts:
    #             account.tags.append(
    #                 Tag(tagname, merchant)
    #             )
