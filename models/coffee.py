class coffee:
    all = []

    def __init__(self, name):
        self.name = name
        coffee.all.append(self)

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
        from models.order import order 
        return [o for o in order.all if o.coffee == self]

    def customers(self):
        return list({o.customer for o in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if orders:
            return sum(o.price for o in orders) / len(orders)
        return 0
