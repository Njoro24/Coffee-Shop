import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def setup_method(self):
        # Reset all lists before each test
        Customer.all = []
        Coffee.all = []
        Order.all = []
        
        # Create test instances
        self.customer = Customer("John")
        self.coffee = Coffee("Espresso")
    
    def test_init(self):
        order = Order(self.customer, self.coffee, 3.5)
        
        assert order.customer == self.customer
        assert order.coffee == self.coffee
        assert order.price == 3.5
        assert order in Order.all
    
    def test_customer_validation(self):
        # Test instance validation
        with pytest.raises(TypeError):
            Order("Not a customer", self.coffee, 3.5)
    
    def test_coffee_validation(self):
        # Test instance validation
        with pytest.raises(TypeError):
            Order(self.customer, "Not a coffee", 3.5)
    
    def test_price_validation(self):
        # Test type validation
        with pytest.raises(TypeError):
            Order(self.customer, self.coffee, "3.5")
        
        # Test range validation
        with pytest.raises(ValueError):
            Order(self.customer, self.coffee, 0.5)  # Below 1.0
        with pytest.raises(ValueError):
            Order(self.customer, self.coffee, 11.0)  # Above 10.0
            
        # Test valid values at boundaries
        order1 = Order(self.customer, self.coffee, 1.0)
        assert order1.price == 1.0
        
        order2 = Order(self.customer, self.coffee, 10.0)
        assert order2.price == 10.0