import datetime

class Transaction:
    def __init__(self, account, merchant, amount, id = None):
        self.account = account
        self.merchant = merchant
        self.amount = amount
        self.timestamp = datetime.datetime.now()
        self.id = id