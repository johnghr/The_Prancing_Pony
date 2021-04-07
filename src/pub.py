from src.drink import Drink
from src.customer import Customer

class Pub:

    def __init__(self, name, till, drink):
        
        self.name = name
        self.till = till
        self.drink = drink

    def add_money_to_till(self, drink):
        self.till += drink.price
        return self.till

    def can_serve_customer(self, age, drunkeness):
        if age >= 18 and drunkeness < 40:  
            return True
        else:
            return False

    def sell_drink_to_customer(self, customer):
        customer.drinks += 1
        return customer.drinks