import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, "Pint of Bree Best")
        self.drink = Drink("Pint of Bree Best", 3.00, 10)
        self.customer = Customer("The Gaffer", 20, 50, 0, 0)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
        
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)
        
    def test_pub_has_drinks(self):
        self.assertEqual("Pint of Bree Best", self.pub.drink)

    def test_money_added_to_till(self):
        self.assertEqual(103, self.pub.add_money_to_till(self.drink))

    def test_can_serve_customer(self):
        self.assertEqual(True, self.pub.can_serve_customer(self.customer.age, self.customer.drunkeness))
    
    def test_customer_has_drunkeness(self):
        self.assertEqual(0, self.customer.drunkeness)

    def test_sell_drink_to_customer(self):
        self.assertEqual(1, self.pub.sell_drink_to_customer(self.customer))

