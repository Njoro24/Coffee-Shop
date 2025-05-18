from customer import Customer
from coffee import Coffee
from order import Order

# Helper function to format prices in Ksh
def format_ksh(amount):
    return f"Ksh {amount:.2f}"

def main():
    # Clear any existing data (in case you run this multiple times)
    Customer.all = []
    Coffee.all = []
    Order.all = []
    
    # Create customers
    Mutiso = Customer("Mutiso")
    Kasongo = Customer("Kasongo")
    Njoro = Customer("Njoro")

    # Create coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    americano = Coffee("Americano")

    # Create orders
    Mutiso.create_order(espresso, 250)
    Mutiso.create_order(latte, 400)
    Mutiso.create_order(espresso, 250)

    Kasongo.create_order(latte, 400)
    Kasongo.create_order(cappuccino, 450)
    Kasongo.create_order(latte, 400)

    Njoro.create_order(americano, 300)
    Njoro.create_order(espresso, 250)
    Njoro.create_order(cappuccino, 450)

    # Demonstrate relationships and methods
    print(f"Mutiso has ordered {len(Mutiso.orders())} coffees")
    print(f"Unique coffee types Mutiso has ordered: {[coffee.name for coffee in Mutiso.coffees()]}")

    print(f"\nLatte orders: {latte.num_orders()}")
    print(f"Latte average price: {format_ksh(latte.average_price())}")
    print(f"Customers who ordered Latte: {[customer.name for customer in latte.customers()]}")

    print(f"\nMost espresso aficionado: {Customer.most_aficionado(espresso).name}")
    print(f"Most latte aficionado: {Customer.most_aficionado(latte).name}")

    # validations checks
    try:
        invalid_customer = Customer("ThisNameIsTooLongForValidation")
    except ValueError as e:
        print(f"\nValidation error: {e}")

   

if __name__ == "__main__":
    main()

