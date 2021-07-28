class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drink(self, drink):
        self.drinks.append(drink)

    def sell_drink(self, drink):
        self.remove_drink(drink)
        self.increase_till(drink)

    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def increase_till(self, drink):
        self.till += drink.price

    def count_drinks(self):
        return len(self.drinks)