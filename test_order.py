import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def setup_method(self):
        Customer.all = []
        Coffee.all = []
        Order.all = []
        self.customer = Customer("Mutiso")
        self.coffee = Coffee("Espresso")

    def test_init(self):
        order = Order(self.customer, self.coffee, 350)
        assert order.customer == self.customer
        assert order.coffee == self.coffee
        assert order.price == 350.0
        assert order in Order.all

    def test_customer_validation(self):
        with pytest.raises(TypeError):
            Order("Not a customer", self.coffee, 350)

    def test_coffee_validation(self):
        with pytest.raises(TypeError):
            Order(self.customer, "Not a coffee", 350)

    def test_price_validation(self):
        # Invalid type
        with pytest.raises(TypeError):
            Order(self.customer, self.coffee, "350")

        # Price just below the allowed range
        with pytest.raises(ValueError):
            Order(self.customer, self.coffee, 199.99)

        # Price just above the allowed range
        with pytest.raises(ValueError):
            Order(self.customer, self.coffee, 1000.01)

        # Valid price values
        order1 = Order(self.customer, self.coffee, 250.0)
        assert order1.price == 250.0

        order2 = Order(self.customer, self.coffee, 450.0)
        assert order2.price == 450.0
