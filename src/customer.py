from src.drink import Drink

class Customer:

    def __init__(self, name, wallet, age, drunkeness, drinks):

        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness
        self.drinks = drinks
    
    def remove_money_from_wallet(self, drink):
        self.wallet -= drink.price
        return self.wallet