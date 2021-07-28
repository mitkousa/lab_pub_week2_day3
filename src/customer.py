class Customer:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drinks = []

    def can_afford_drink(self, drink):
        if self.wallet > drink.price:
            return True
        else:
            return False

    def add_drink(self, drink):
        self.drinks.append(drink)
        
    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def buy_drink(self):
        pass