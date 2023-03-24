import unittest

# Add imports here
from models.merchant import Merchant
from models.tag import Tag
from models.bank import Bank

class TestBank(unittest.TestCase):

    def setUp(self):
        self.bnk1 = Bank("Bank of Blood")
        self.bnk2 = Bank("The Casino Bank")


    def test_bank_has_names(self):
        self.assertEqual("Bank of Blood", self.bnk1.name)
        self.assertEqual("The Casino Bank", self.bnk2.name)

    def test_bank_initially_has_none_for_id(self):
        self.assertEqual(None, self.bnk1.id)
        self.assertEqual(None, self.bnk2.id)

    def test_bank_can_tag_merchant(self):
        mct1 = Merchant("Server Farm")
        self.assertEqual(0, len(self.bnk1.tags))
        self.bnk1.tag_merchant("Electronics", mct1)
        self.assertEqual(1, len(self.bnk1.tags))