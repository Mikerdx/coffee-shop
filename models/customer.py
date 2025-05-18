class customer:
    all = []

    def __init__(self, name):
        self.name = name
        customer.all.append(self)

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
        from models.order import order
        return [o for o in order.all if o.customer == self]

    def coffees(self):
        from models.order import order
        return list({o.coffee for o in self.orders()})

    def create_order(self, coffee, price):
        from models.order import order
        return order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from models.order import order  # ✅ Delayed import
        customer_spend = {}
        for o in order.all:
            if o.coffee == coffee:
                customer_spend[o.customer] = customer_spend.get(o.customer, 0) + o.price
        return max(customer_spend, key=customer_spend.get, default=None)
