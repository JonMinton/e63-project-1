import datetime

class Transaction:
    def __init__(self, account, merchant, amount, timestamp = datetime.datetime.now(), id = None):
        self.account = account
        self.merchant = merchant
        self.amount = amount
        self.timestamp = timestamp
        self.id = id