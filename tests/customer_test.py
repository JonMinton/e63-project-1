import unittest

# Add imports here
from models.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.cst1 = Customer("Jon", "Minton")
        self.cst2 = Customer("Mon", "Jinton")
        # Add setup assets here
        # self.fake_loc = "path/to/nowhere"
        # self.my_lib = Library("My first occult library")

    def test_customers_have_names(self):
        self.assertEqual("Jon", self.cst1.first_name)
        self.assertEqual("Minton", self.cst1.last_name)
        self.assertEqual("Mon", self.cst2.first_name)
        self.assertEqual("Jinton", self.cst2.last_name)
