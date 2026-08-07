# Mini Banking System Using Python

A modular **Mini Banking System** developed using **Core Python** without Object-Oriented Programming (OOP). This project demonstrates how to build a real-world banking application using Python functions, modules, dictionaries, exception handling, logging, and file handling.

---

## Project Overview

This project simulates the basic functionalities of a banking system. It is designed to help beginners understand how to organize a Python project into multiple modules while following clean coding practices.

---

## Features

- Create Customer Account
- Deposit Money
- Withdraw Money
- Transfer Money
- Check Account Balance
- Generate Unique Account Number
- Validate User Inputs
- Custom Exception Handling
- Log Successful and Failed Transactions
- Generate Transaction Report
- View Transaction Log

---

## Project Structure

```
Mini_Banking_System/

│── main.py
│── customers.py
│── transactions.py
│── validation.py
│── exceptions.py
│── utils.py
│── logger.py
│── data.py
│── banklog.txt
│── README.md
```

---

## Modules Description

### `main.py`

Acts as the entry point of the application. Displays the banking menu and calls the required functions.

### `customers.py`

Contains all customer-related operations.

- Create Customer
- Generate Unique Account Number
- Store Customer Details

### `transactions.py`

Contains all banking operations.

- Deposit
- Withdraw
- Transfer Money
- Check Balance
- Generate Transaction Report
- View Transaction Logs

### `validation.py`

Validates user input before processing.

- Validate Account Number
- Validate Amount
- Validate Balance

### `exceptions.py`

Defines custom exceptions.

- InvalidAmountError
- InsufficientBalanceError
- InvalidAccountNumber

### `utils.py`

Contains reusable helper functions.

- Generate Account Number
- Check Account Existence

### `logger.py`

Configures the logging system.

- get_logger()
- FileHandler
- Formatter

### `data.py`

Stores customer data using a dictionary.

---

## Concepts Used

- Python Functions
- Modular Programming
- Dictionaries
- Loops
- Conditional Statements
- Input Validation
- Exception Handling
- Custom Exceptions
- Logging Module
- File Handling
- Code Reusability
- Project Structure

---

## Logging

Every successful and failed transaction is recorded in **banklog.txt**.

Example log:

```
07-08-2026 18:30:45 | INFO | BankingSystem | Deposit Successful | Account:1234 | Amount:5000

07-08-2026 18:35:10 | ERROR | BankingSystem | Withdrawal Failed | Insufficient Balance
```

---

## Transaction Report

The application generates a transaction report by analyzing the log file.

The report includes:

- Total Deposits
- Total Withdrawals
- Total Transfers
- Successful Transactions
- Failed Transactions

---

## Technologies Used

- Python 3
- Logging Module
- File Handling
- Exception Handling

---

## Learning Outcomes

By completing this project, you will learn how to:

- Organize a Python project into multiple modules
- Build reusable functions
- Implement input validation
- Create custom exceptions
- Configure and use Python logging
- Handle runtime errors effectively
- Generate reports from log files
- Develop a menu-driven application

---

## How to Run

Clone the repository.

```bash
git clone <repository_url>
```

Navigate to the project directory.

```bash
cd Mini_Banking_System
```

Run the application.

```bash
python main.py
```

---

## Author

**Yamuna**

Python | Machine Learning | Data Analytics 
---

## License

This project is created for educational purposes and learning Core Python through a real-world application.
