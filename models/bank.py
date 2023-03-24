class Bank:
    def __init__(self, name, id = None):
        self.name = name
        self.accounts = []
        self.id = id

    def get_num_accounts(self):
        return len(self.accounts)
        
