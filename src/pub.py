class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drink(self, drink):
        self.drinks.append(drink.name)

    def sell_drink(self):
        pass

    def remove_drink(self):
        pass

    def increase_till(self):
        pass