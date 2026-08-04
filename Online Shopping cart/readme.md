# Royal Electronics Market - Shopping Cart System

## Description

Royal Electronics Market is a console-based shopping cart application developed using Python. The application allows customers to purchase electronic products, validates user input, manages product inventory, applies discounts based on the purchase amount, and generates a detailed invoice.

This project demonstrates the implementation of core Python concepts through a real-world shopping cart simulation.

---

## Features

- Interactive menu-driven application
- Browse and purchase electronic products
- Add multiple products to the shopping cart
- Prevent invalid product selection
- Validate purchase quantity
- Check available stock before purchase
- Automatically update inventory after purchase
- Continue shopping until checkout
- Calculate subtotal
- Apply discounts based on purchase amount
- Generate a formatted customer invoice
- Cancel or confirm purchase before payment

---

## Available Products

| Product | Price (₹) | Available Stock |
|---------|----------:|----------------:|
| Laptop | 65,000 | 5 |
| Phone | 25,000 | 3 |
| Mouse | 800 | 4 |
| Keyboard | 1,200 | 8 |
| Monitor | 9,000 | 2 |
| Speaker | 2,500 | 7 |
| Headphone | 1,500 | 9 |
| Pen Drive | 2,500 | 4 |

---

## Discount Rules

| Purchase Amount | Discount |
|----------------:|---------:|
| Above ₹10,000 | 5% |
| Above ₹30,000 | 10% |
| Above ₹60,000 | 15% |

---

## Technologies Used

- Python 3

---

## Python Concepts Covered

- Variables
- Dictionaries
- Nested Dictionaries
- Loops (`while`, `for`)
- Conditional Statements
- Input Validation
- String Manipulation
- Arithmetic Operations
- Menu-Driven Programming
- Inventory Management
- Invoice Generation

---

## Project Structure

```text
Royal-Electronics-Market/
│
├── shopping_cart.py
└── README.md
```

---

## How to Run

1. Install Python 3 on your computer.
2. Clone this repository or download the project files.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python shopping_cart.py
```

---

## Application Workflow

1. Display the main menu.
2. Select **Shop**, **Check Offers**, or **Exit**.
3. Enter the product name.
4. View the product price and available stock.
5. Enter the desired quantity.
6. Add products to the shopping cart.
7. Continue shopping or proceed to checkout.
8. View the invoice.
9. Confirm or cancel the purchase.

---

## Sample Invoice

```text
=========================================================
                    FINAL INVOICE
=========================================================

Item           Quantity   Price          Total
---------------------------------------------------------
Laptop         1          ₹65000         ₹65000
Mouse          2          ₹800           ₹1600
Keyboard       1          ₹1200          ₹1200

---------------------------------------------------------
Subtotal                ₹67800
Discount (15%)          ₹10170
---------------------------------------------------------
Final Amount            ₹57630
=========================================================
```

---

## Data Structures Used

### Product Catalog

```python
products_data = {
    "laptop": {
        "price": 65000,
        "quantity": 5
    }
}
```

### Shopping Cart

```python
cart = {
    "laptop": {
        "quantity": 1,
        "price": 65000
    }
}
```

### Discount Mapping

```python
discount_data = {
    10000: 5,
    30000: 10,
    60000: 15
}
```

---

## Input Validation

The application validates:

- Menu selection
- Product availability
- Quantity greater than zero
- Quantity should not exceed available stock
- Purchase confirmation before checkout


## Learning Outcomes

This project demonstrates practical experience in:

- Building menu-driven applications
- Managing inventory using nested dictionaries
- Implementing shopping cart functionality
- Applying business logic such as discounts
- Generating formatted invoices
- Performing data validation
- Writing structured and maintainable Python programs

Link: https://github.com/yamunah96/Python-classes/tree/main/Online%20Shopping%20cart

---
