import repositories.merchant_repository as merchant_repository


class Merchant():
    def __init__(self, name, num_sales = 0, revenue = 0.0, id = None):
        self.name = name
        self.num_sales = num_sales
        self.revenue = revenue
        self.id = id

        if self.id == None:
            assigned_id = merchant_repository.init_save_get_id(
                self.name, 
                self.num_sales,
                self.revenue
            )
            self.id = assigned_id

    # I'm going to assume the destroctor method is implicitly invoked 
    # whenever an object of this class disappears
    def __del__(self):
        merchant_repository.delete(self.id)