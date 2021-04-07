import unittest
from src.drink import Drink 

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Pint of Bree Best", 3, 8)

    def test_drink_has_name(self):
        self.assertEqual("Pint of Bree Best", self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(3, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(8, self.drink.alcohol_level)
        