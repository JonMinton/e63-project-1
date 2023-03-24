import unittest

# Add imports here
from models.merchant import Merchant
from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.merc1 = Merchant("Winos")
        self.merc2 = Merchant("Cheesy Chippie")
        self.merc3 = Merchant("Lidaldi")
        self.tag1 = Tag("Bar", self.merc1)
        self.tag2 = Tag("Restaurant", self.merc1)
        self.tag3 = Tag("Take-away", self.merc2)
        self.tag4 = Tag("Groceries", self.merc3)

    # Add specific tests here
    def test_tags_have_correct_properties(self):
        self.assertEqual(
            "Bar",
            self.tag1.name
        )
        self.assertEqual(
            "Take-away",
            self.tag3.name
        )
        self.assertEqual(
            "Lidaldi",
            self.tag4.merchant.name
        )
