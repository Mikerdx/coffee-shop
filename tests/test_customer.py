import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import unittest
from models.coffee import Coffee
from models.customer import Customer
from models.order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Coffee.all.clear()
        Customer.all.clear()
        Order.all.clear()
        self.customer = Customer("Anna")
        self.coffee1 = Coffee("Latte")
        self.coffee2 = Coffee("Mocha")
        Order(self.customer, self.coffee1, 6.0)
        Order(self.customer, self.coffee2, 4.0)

    def test_customer_name(self):
        self.assertEqual(self.customer.name, "Anna")

    def test_orders_method(self):
        self.assertEqual(len(self.customer.orders()), 2)

    def test_coffees_method(self):
        self.assertIn(self.coffee1, self.customer.coffees())
        self.assertIn(self.coffee2, self.customer.coffees())

    def test_create_order(self):
        coffee = Coffee("Americano")
        order = self.customer.create_order(coffee, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_most_aficionado(self):
        customer2 = Customer("Lina")
        Order(customer2, self.coffee1, 8.0)
        self.assertEqual(Customer.most_aficionado(self.coffee1), customer2)

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("A" * 16)

if __name__ == "__main__":
    unittest.main()
