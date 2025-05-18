class order:
    all = []

    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None

        self.customer = customer
        self.coffee = coffee
        self.price = price

        order.all.append(self)
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from customer import customer
        if not isinstance(value, customer):
            raise TypeError("Customer must be a customer instance")
        
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from coffee import coffee
        if not isinstance(value, coffee):
            raise TypeError("Coffee must be a coffee instance")
        
        self._coffee = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        
        self._price = float(value)

