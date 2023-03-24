import unittest

# Add imports here
from models.bank import Bank

class TestBank(unittest.TestCase):

    def setUp(self):
        self.bnk1 = Bank("Bank of Blood")
        self.bnk2 = Bank("The Casino Bank")


    def test_banks_have_names(self):
        self.assertEqual("Bank of Blood", self.bnk1.name)
        self.assertEqual("The Casino Bank", self.bnk2.name)

    def test_banks_initially_have_none_for_id(self):
        self.assertEqual(None, self.bnk1.id)
        self.assertEqual(None, self.bnk2.id)