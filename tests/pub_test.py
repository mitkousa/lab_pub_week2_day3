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
        self.assertEqual("Coke", self.drink.name)



