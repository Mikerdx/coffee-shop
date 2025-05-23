import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import unittest
from models.coffee import Coffee
from models.customer import Customer
from models.order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Coffee.all.clear()
        Customer.all.clear()
        Order.all.clear()
        self.customer = Customer("Eli")
        self.coffee = Coffee("Cappuccino")
        self.order = Order(self.customer, self.coffee, 7.0)

    def test_order_instance(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.coffee, self.coffee)
        self.assertEqual(self.order.price, 7.0)

    def test_invalid_customer(self):
        with self.assertRaises(TypeError):
            Order("NotACustomer", self.coffee, 5.0)

    def test_invalid_coffee(self):
        with self.assertRaises(TypeError):
            Order(self.customer, "NotACoffee", 5.0)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)

if __name__ == "__main__":
    unittest.main()
