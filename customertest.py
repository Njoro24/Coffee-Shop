import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def setup_method(self):
        # Reset all lists before each test
        Customer.all = []
        Coffee.all = []
        Order.all = []
        
        # Create test instances
        self.customer1 = Customer("Mutiso")
        self.customer2 = Customer("Kasongo")
        self.coffee1 = Coffee("Espresso")
        self.coffee2 = Coffee("Latte")
    
    def test_init(self):
        assert self.customer1.name == "John"
        assert self.customer1 in Customer.all
    
    def test_name_validation(self):
        # Test string validation
        with pytest.raises(TypeError):
            Customer(123)
        
        # Test length validation
        with pytest.raises(ValueError):
            Customer("")
        with pytest.raises(ValueError):
            Customer("ThisNameIsTooLong1234")
    
    def test_orders(self):
        order1 = Order(self.customer1, self.coffee1, 350)
        order2 = Order(self.customer1, self.coffee2, 45)
        order3 = Order(self.customer2, self.coffee1, 350)
        
        assert len(self.customer1.orders()) == 2
        assert order1 in self.customer1.orders()
        assert order2 in self.customer1.orders()
        assert order3 not in self.customer1.orders()
    
    def test_coffees(self):
        Order(self.customer1, self.coffee1, 350)
        Order(self.customer1, self.coffee2, 450)
        Order(self.customer1, self.coffee1, 350)
        
        customer_coffees = self.customer1.coffees()
        assert len(customer_coffees) == 2
        assert self.coffee1 in customer_coffees
        assert self.coffee2 in customer_coffees
    
    def test_create_order(self):
        order = self.customer1.create_order(self.coffee1, 350)
        
        assert isinstance(order, Order)
        assert order.customer == self.customer1
        assert order.coffee == self.coffee1
        assert order.price == 350
    
    def test_most_aficionado(self):
        # Customer1 spends more on coffee1
        Order(self.customer1, self.coffee1, 450)
        Order(self.customer1, self.coffee1, 350)
        Order(self.customer2, self.coffee1, 350)
        
        # Customer2 spends more on coffee2
        Order(self.customer1, self.coffee2, 800)
        Order(self.customer2, self.coffee2, 450)
        Order(self.customer2, self.coffee2, 900)
        
        assert Customer.most_aficionado(self.coffee1) == self.customer1
        assert Customer.most_aficionado(self.coffee2) == self.customer2
        
        # Test with a coffee no one has ordered
        coffee3 = Coffee("Mocha")
        assert Customer.most_aficionado(coffee3) is None