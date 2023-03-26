from models.merchant import Merchant
from models.tag import Tag

class Bank:
    def __init__(self, name, id = None):
        self.name = name
        self.customers = []
        self.tags = []
        self.id = id

    # def get_num_accounts(self):
    #     return len(self.accounts)
    
    def tag_merchant(self, tagname, merchant):
        self.tags.append(
            Tag(tagname, merchant)
        )
        
    def get_num_customers(self):
        return len(self.customers)
    
    def get_num_accounts(self):
        return sum(
            [len(customer.accounts) for customer in self.customers]
        )