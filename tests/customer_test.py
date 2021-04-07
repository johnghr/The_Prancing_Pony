import unittest
from src.customer import Customer 
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("The Gaffer", 20, 51, 0, 0)

    def test_customer_has_name(self):
        self.assertEqual("The Gaffer", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)

    def test_remove_money_from_wallet(self):
        drink = Drink("Pint of Bree Best", 3, 10)
        self.assertEqual(17, self.customer.remove_money_from_wallet(drink))
    
    def test_customer_has_age(self):
        self.assertEqual(51, self.customer.age)

    