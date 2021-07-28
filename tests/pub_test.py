import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Coke", 2)
        self.pub = Pub("The Prancing Pony", 100)
        self.customer = Customer("John", 100)

    def test_pub_has_name(self): 
        self.assertEqual("The Prancing Pony", self.pub.name) 

    def test_add_drink(self):
        self.pub.add_drink(self.drink)
        self.assertEqual(1, self.pub.count_drinks())

    def test_remove_drink(self):
        self.pub.add_drink(self.drink)
        self.pub.remove_drink(self.drink)
        self.assertEqual(0, self.pub.count_drinks())

    def test_increase_till(self):
        self.pub.increase_till(self.drink)
        self.assertEqual(102, self.pub.till)

    def test_sell_drink(self):
        self.pub.add_drink(self.drink)
        self.pub.sell_drink(self.drink)
        self.assertEqual(102, self.pub.till)
        self.assertEqual(0, self.pub.count_drinks())


