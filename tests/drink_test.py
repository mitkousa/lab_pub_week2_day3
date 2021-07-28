import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Coke", 2)
        self.pub = Pub("The Prancing Pony", 100)
        self.customer = Customer("John", 100)

    def test_drink_has_name(self):
        self.assertEqual("Coke", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(2, self.drink.price)
    