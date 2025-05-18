class coffee:
    all = []

    def __init__(self, name):
        self.name = None
        self.name = name
        coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.settert
    def name (self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = value
        
    def orders(self):
        from order import order
        return [order for order in order.all if order.coffee == self]
    
    #list of customers who ordered this coffee
    def customers(self):
        from customer import customer
        return list({order.customer for order in self.orders()})
    
    #returns total number of orders for this coffee
    def num_orders(self):
        return len(self.orders())
    
    #returns average price of this coffee
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)

    