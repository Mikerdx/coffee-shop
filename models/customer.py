class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        from models.order import Order
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        from models.order import Order
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from models.order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from models.order import Order
        customer_spend = {}
        for order in Order.all:
            if order.coffee == coffee:
                customer_spend[order.customer] = customer_spend.get(order.customer, 0) + order.price
        # Return customer who spent the most on the coffee or None if no orders
        return max(customer_spend, key=customer_spend.get, default=None)
