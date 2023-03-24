from models.transaction import Transaction
class Account():
    def __init__(self, bank, customer, balance = 0.0, id = None):
        self.bank = bank
        self.customer = customer
        self.balance = balance
        self.transactions = []
        self.tags = bank.tags
        self.id = id

    def return_balance(self):
        return self.balance
    
    def deposit_monies(self, amt):
        self.balance += amt

    def make_transaction(self, merchant, amount):
        if self.balance > amount:
            self.transactions.append(
                Transaction(self, merchant, amount)
            )
            self.balance -= amount