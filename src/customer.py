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

    def buy_drink(self, drink):
        if self.can_afford_drink == True:
            self.add.drink(self.drinks)
            self.reduce.wallet(drink.price)

    def count_drinks(self):
        return len(self.drinks)