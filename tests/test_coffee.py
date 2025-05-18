import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.customer import customer
from models.coffee import coffee
from models.order import order

class TestCoffee(unittest.TestCase):

    def setUp(self):
        customer.all.clear()
        coffee.all.clear()
        order.all.clear()
        self.cust = customer("Anna")
        self.coffee = coffee("Cappuccino")

    def test_coffee_created(self):
        self.assertEqual(self.coffee.name, "Cappuccino")

    def test_num_orders(self):
        self.cust.create_order(self.coffee, 4.0)
        self.cust.create_order(self.coffee, 6.0)
        self.assertEqual(self.coffee.num_orders(), 2)

    def test_average_price(self):
        self.cust.create_order(self.coffee, 4.0)
        self.cust.create_order(self.coffee, 6.0)
        self.assertAlmostEqual(self.coffee.average_price(), 5.0)

if __name__ == '__main__':
    unittest.main()
