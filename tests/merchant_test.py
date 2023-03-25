import unittest

# Add imports here
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.mct1 = Merchant("Grubby Grubs")


    def test_merchants_have_names(self):
        self.assertEqual("Grubby Grubs", self.mct1.name)

    def test_merchants_initially_have_no_revenue_by_default(self):
        self.assertEqual(0.0, self.mct1.revenue)

    def test_merchants_initially_have_no_sales(self):
        self.assertEqual(0, self.mct1.num_sales)


