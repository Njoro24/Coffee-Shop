class Customer:
    all = []
    
    def __init__(self, name):
        self._name = name
        self.name = name
        Customer.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (4 <= len(value) < 20):
             raise ValueError("Name must be between 4 and 19 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        # Return a unique list of Coffee instances that the customer has ordered
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        # Find the customer who has spent the most on the given coffee
        coffee_customers = {}
        
        from order import Order
        coffee_orders = [order for order in Order.all if order.coffee == coffee]
        
        if not coffee_orders:
            return None
            
        for order in coffee_orders:
            customer = order.customer
            if customer not in coffee_customers:
                coffee_customers[customer] = 0
            coffee_customers[customer] += order.price
            
        # Return the customer who spent the most
        return max(coffee_customers.items(), key=lambda x: x[1])[0]