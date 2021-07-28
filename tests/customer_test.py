import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Coke", 2)
        self.pub = Pub("The Prancing Pony", 100)
        self.customer = Customer("John", 100)

    def test_customer_has_name(self): 
        self.assertEqual("John", self.customer.name)

    def test_customer_has_wallet(self): 
        self.assertEqual(100, self.customer.wallet)
    
    def test_can_afford_drink(self):
        self.assertEqual(True, self.customer.can_afford_drink(self.drink))

    def test_can_afford_drink__false(self):
        expensive = Drink("Name of", 2000)
        self.assertEqual(False, self.customer.can_afford_drink(expensive))

    def test_add_drink(self):
        self.customer.add_drink(self.drink)
        self.assertEqual(1, self.customer.count_drinks())

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(self.drink)
        self.assertEqual(98, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.add_drink()

