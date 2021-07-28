import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Coke", 2)
        self.pub = Pub("The Prancing Pony", 100)
        self.customer = Customer("John", 100)

    def test_can_afford_drink(self):
        self.assertEqual(True, self.drink())

    def test_buy_drink(self):
         self.assertEqual(())