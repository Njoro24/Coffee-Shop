import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    def setup_method(self):
        # Reset all lists before each test
        Customer.all = []
        Coffee.all = []
        Order.all = []
        
        # Create test instances
        self.coffee1 = Coffee("Espresso")
        self.coffee2 = Coffee("Latte")
        self.customer1 = Customer("John")
        self.customer2 = Customer("Jane")
    
    def test_init(self):
        assert self.coffee1.name == "Espresso"
        assert self.coffee1 in Coffee.all
    
    def test_name_validation(self):
        # Test string validation
        with pytest.raises(TypeError):
            Coffee(123)
        
        # Test length validation
        
        with pytest.raises(ValueError):
            Coffee("AB")
    
    def test_orders(self):
        order1 = Order(self.customer1, self.coffee1, 350)
        order2 = Order(self.customer2, self.coffee1, 450)
        order3 = Order(self.customer1, self.coffee2, 350)
        
        coffee1_orders = self.coffee1.orders()
        assert len(coffee1_orders) == 2
        assert order1 in coffee1_orders
        assert order2 in coffee1_orders
        assert order3 not in coffee1_orders
    
    def test_customers(self):
        Order(self.customer1, self.coffee1, 350)
        Order(self.customer2, self.coffee1, 450)
        Order(self.customer1, self.coffee1, 350)  
        
        coffee_customers = self.coffee1.customers()
        assert len(coffee_customers) == 2
        assert self.customer1 in coffee_customers
        assert self.customer2 in coffee_customers
    
    def test_num_orders(self):
        assert self.coffee1.num_orders() == 0
        
        Order(self.customer1, self.coffee1, 350)
        assert self.coffee1.num_orders() == 1
        
        Order(self.customer2, self.coffee1, 450)
        assert self.coffee1.num_orders() == 2
    
    def test_average_price(self):
        assert self.coffee1.average_price() == 0  # No orders yet
        
        Order(self.customer1, self.coffee1, 350)
        assert self.coffee1.average_price() == 350
        
        Order(self.customer2, self.coffee1, 800)
        assert self.coffee1.average_price() == 450