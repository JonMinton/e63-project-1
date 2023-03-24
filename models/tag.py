import datetime

class Tag:
    def __init__(self, name, merchant, timestamp = None, id = None):
        self.name = name
        self.merchant = merchant
        self.timestamp = datetime.datetime.now()
        self.id = id