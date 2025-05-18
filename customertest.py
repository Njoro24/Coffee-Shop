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
        self.customer1 = Customer("John")
        self.customer2 = Customer("Jane")
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
        order1 = Order(self.customer1, self.coffee1, 3.5)
        order2 = Order(self.customer1, self.coffee2, 4.5)
        order3 = Order(self.customer2, self.coffee1, 3.5)
        
        assert len(self.customer1.orders()) == 2
        assert order1 in self.customer1.orders()
        assert order2 in self.customer1.orders()
        assert order3 not in self.customer1.orders()
    
    def test_coffees(self):
        Order(self.customer1, self.coffee1, 3.5)
        Order(self.customer1, self.coffee2, 4.5)
        Order(self.customer1, self.coffee1, 3.0)  # Duplicate coffee shouldn't count twice
        
        customer_coffees = self.customer1.coffees()
        assert len(customer_coffees) == 2
        assert self.coffee1 in customer_coffees
        assert self.coffee2 in customer_coffees
    
    def test_create_order(self):
        order = self.customer1.create_order(self.coffee1, 3.5)
        
        assert isinstance(order, Order)
        assert order.customer == self.customer1
        assert order.coffee == self.coffee1
        assert order.price == 3.5
    
    def test_most_aficionado(self):
        # Customer1 spends more on coffee1
        Order(self.customer1, self.coffee1, 4.0)
        Order(self.customer1, self.coffee1, 3.5)
        Order(self.customer2, self.coffee1, 3.0)
        
        # Customer2 spends more on coffee2
        Order(self.customer1, self.coffee2, 2.0)
        Order(self.customer2, self.coffee2, 4.0)
        Order(self.customer2, self.coffee2, 5.0)
        
        assert Customer.most_aficionado(self.coffee1) == self.customer1
        assert Customer.most_aficionado(self.coffee2) == self.customer2
        
        # Test with a coffee no one has ordered
        coffee3 = Coffee("Mocha")
        assert Customer.most_aficionado(coffee3) is None