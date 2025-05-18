import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.customer import customer
from models.coffee import coffee
from models.order import order

class TestCustomer(unittest.TestCase):

    def setUp(self):
        customer.all.clear()
        coffee.all.clear()
        order.all.clear()
        self.cust = customer("Mike")
        self.coffee1 = coffee("Espresso")
        self.coffee2 = coffee("Latte")

    def test_customer_created(self):
        self.assertEqual(self.cust.name, "Mike")

    def test_create_order(self):
        o = self.cust.create_order(self.coffee1, 5.0)
        self.assertEqual(o.customer, self.cust)
        self.assertEqual(o.coffee, self.coffee1)
        self.assertEqual(o.price, 5.0)

    def test_coffees(self):
        self.cust.create_order(self.coffee1, 5.0)
        self.cust.create_order(self.coffee2, 6.0)
        coffee_names = [c.name for c in self.cust.coffees()]
        self.assertIn("Espresso", coffee_names)
        self.assertIn("Latte", coffee_names)

if __name__ == '__main__':
    unittest.main()
