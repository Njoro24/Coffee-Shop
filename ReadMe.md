# Coffee Shop Domain Model
This project implements a domain model for a Coffee Shop using object-oriented programming principles in Python.
Project Structure
coffee_shop/
├── customer.py
├── coffee.py
├── order.py
├── debug.py
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
├── Pipfile
└── README.md
## Domain Model
The application models a Coffee Shop with three main entities:

### Customer: Represents a coffee shop customer
### Coffee: Represents a coffee product
### Order: Represents an order made by a customer for a specific coffee

## Relationships

A Customer can place many Orders
A Coffee can have many Orders
An Order belongs to one Customer and one Coffee

## Setup Instructions

Clone the repository
Set up a virtual environment:

bashpipenv install
pipenv shell

Install pytest:

bashpipenv install pytest

## Running the Application
You can test the application using the debug script:
bashpython debug.py
Running Tests
Run all tests:
bashpytest
Run tests for a specific class:
bashpytest tests/test_customer.py

## Classes and Methods
### Customer Class

Attributes: name (string between 1 and 15 characters)
Methods:

orders(): Returns all orders placed by the customer
coffees(): Returns all unique coffees ordered by the customer
create_order(coffee, price): Creates a new order for the customer
most_aficionado(coffee): Class method that returns the customer who spent the most on a given coffee



### Coffee Class

Attributes: name (string, at least 3 characters)
Methods:

orders(): Returns all orders for this coffee
customers(): Returns all unique customers who ordered this coffee
num_orders(): Returns the total number of orders for this coffee
average_price(): Returns the average price of orders for this coffee



### Order Class

Attributes: customer, coffee, price (float between 1.0 and 10.0)
Properties:

customer: Returns the associated Customer instance
coffee: Returns the associated Coffee instance
price: Returns the price of the order



## Implementation Details

All classes implement proper validation for their attributes
Exception handling is implemented for invalid inputs
The code follows PEP 8 guidelines for clean and readable code
