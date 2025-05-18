from models.customer import customer
from models.coffee import coffee
from models.order import order


c1 = customer("Mike")
c2 = customer("Jane")
coffee1 = coffee("Espresso")
coffee2 = coffee("Latte")

c1.create_order(coffee1, 5.5)
c1.create_order(coffee2, 6.0)
c2.create_order(coffee1, 9.0)

print(f"{c1.name}'s Coffees: {[c.name for c in c1.coffees()]}")
print(f"{coffee1.name} has {coffee1.num_orders()} orders.")
print(f"Average price of {coffee1.name}: {coffee1.average_price()}")

aficionado = customer.most_aficionado(coffee1)
print(f"Most aficionado for {coffee1.name}: {aficionado.name if aficionado else 'None'}")
