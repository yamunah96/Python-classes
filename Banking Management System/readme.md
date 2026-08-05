# HDFC Bank Management System

## Overview

This is a simple Python-based Bank Management System that performs basic banking operations using Python dictionaries. The project runs in the terminal and stores account details in memory during program execution.

The application allows users to:

- Create a bank account
- Deposit money
- Withdraw money
- Check account balance
- Transfer money between accounts
- Display all customer accounts
- Calculate the total money stored in the bank
- Display the richest customer

---

## Features

### 1. Create Account

- Creates a new customer account.
- Generates a random 5-digit account number.
- Initial balance is set to **1000 Rupees**.
- Prevents duplicate customer names.

---

### 2. Deposit

- Deposits money into an existing account.
- Validates that the entered amount is greater than zero.

---

### 3. Withdraw

- Withdraws money from an account.
- Checks whether sufficient balance is available.
- Prevents negative withdrawals.

---

### 4. Check Balance

- Displays the current balance using the account number.

---

### 5. Transfer Money

- Transfers money from one customer to another.
- Verifies both sender and receiver account details.
- Ensures sufficient balance before transfer.

---

### 6. Show All Accounts

Displays all customer details including:

- Customer Name
- Account Number
- Account Balance

---

### 7. Exit

Ends the program.

After exiting, the program displays:

- Total money stored in the bank
- Richest customer

---

## Data Structure

Customer information is stored in a nested dictionary.

Example:

```python
accounts = {
    "yamuna": {
        "account_number": "12345",
        "balance": 5000
    },
    "shiva": {
        "account_number": "67890",
        "balance": 3000
    }
}
```

---

## Technologies Used

- Python 3
- Dictionary
- Loops
- Conditional Statements
- Random Module
- User Input

---

## Program Flow

```
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transfer Money
6. Show All Accounts
7. Exit
```

---

## Output After Exit

The program calculates:

- Total amount stored in the bank
- Customer with the highest account balance

---

## File

```
bank_management_system.py
```
# Link
https://youtu.be/stR45gqui8g

---

## Author

Yamuna
