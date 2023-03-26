from models.transaction import Transaction

class Account():
    def __init__(self, balance = 0.0, id = None):
        self.balance = balance
        self.id = id

    def return_balance(self):
        return self.balance
    
    # def deposit_monies(self, amt):
    #     self.balance += amt

    # def make_transaction(self, merchant, amount):
    #     if self.balance > amount:
    #         self.transactions.append(
    #             Transaction(self, merchant, amount)
    #         )
    #         self.balance -= amount