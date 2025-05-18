import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.customer import customer
from models.coffee import coffee
from models.order import order

class TestOrder(unittest.TestCase):

    def setUp(self):
        customer.all.clear()
        coffee.all.clear()
        order.all.clear()
        self.cust = customer("Tom")
        self.coffee = coffee("Mocha")
        self.order = order(self.cust, self.coffee, 7.0)

    def test_order_attributes(self):
        self.assertEqual(self.order.customer.name, "Tom")
        self.assertEqual(self.order.coffee.name, "Mocha")
        self.assertEqual(self.order.price, 7.0)

if __name__ == '__main__':
    unittest.main()
