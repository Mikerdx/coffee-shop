class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Coffee name must be a non-empty string.")

    def orders(self):
        from models.order import Order
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        # Return unique customers who ordered this coffee
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if orders:
            return sum(order.price for order in orders) / len(orders)
        return 0.0
