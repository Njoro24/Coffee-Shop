from customer import Customer
from coffee import Coffee

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")

        price = float(price)
        if not 200 <= price <= 1000:
            raise ValueError("price must be between 200 and 1000")

        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all.append(self)