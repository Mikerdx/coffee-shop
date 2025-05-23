import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from models.coffee import Coffee
from models.customer import Customer
from models.order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Coffee.all.clear()
        Customer.all.clear()
        Order.all.clear()
        self.coffee = Coffee("Espresso")
        self.customer = Customer("Mike")
        Order(self.customer, self.coffee, 5.0)
        Order(self.customer, self.coffee, 3.0)

    def test_coffee_instance(self):
        self.assertEqual(self.coffee.name, "Espresso")

    def test_orders_method(self):
        self.assertEqual(len(self.coffee.orders()), 2)

    def test_customers_method(self):
        self.assertEqual(self.coffee.customers(), [self.customer])

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 2)

    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 4.0)

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError):
            Coffee("")

if __name__ == "__main__":
    unittest.main()
