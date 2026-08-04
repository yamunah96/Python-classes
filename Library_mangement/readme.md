# 📚 Karnataka Government Public Library Management System

A simple **Library Management System** developed using **basic Python programming concepts**. This project is designed for beginners who are learning Python and demonstrates how to build a menu-driven application without using functions or object-oriented programming.

---

## 📖 Project Overview

The Library Management System allows users to:

- Add new books to the library
- Update existing book details
- Borrow available books
- Return borrowed books
- Search for books
- Display all books in the library
- View borrowed books
- Exit the application

The program stores all data using Python dictionaries and runs continuously using a `while` loop until the user chooses to exit.

---

## 🚀 Features

### 1. Add Book
- Add a new book to the library.
- If the book already exists, the user can update:
  - Author
  - Description
  - Genre

### 2. Borrow Book
- Borrow a book if it is available.
- Updates the book status to **Unavailable**.
- Stores the borrower's name.

### 3. Return Book
- Return a borrowed book.
- Updates the status back to **Available**.

### 4. Search Book
- Search for a book by its name.
- Displays:
  - Author
  - Description
  - Availability Status
- If the book is not found, similar book names are suggested.

### 5. Display Books
Shows:
- Total number of books
- Available books
- Unavailable books

Also displays complete details of every book.

### 6. Borrowed Books
Displays all currently borrowed books along with the borrower's name.

### 7. Exit
Terminates the application.

---

## 💻 Technologies Used

- Python 3
- Command Line Interface (CLI)

---

## 📂 Data Structures Used

### Dictionary

The project uses Python dictionaries to store data.

### Books Dictionary

```python
books_data = {
    "book_name": {
        "author": "...",
        "description": "...",
        "genre": "...",
        "status": "available"
    }
}
```

### Borrowed Books Dictionary

```python
borrowed_data = {
    "book_name": {
        "borrower_name": "..."
    }
}
```

---

## 🧠 Python Concepts Used

This project is built using only **basic Python concepts**.

- Variables
- Dictionaries
- Nested Dictionaries
- if, elif, else statements
- while loop
- for loop
- User Input (`input()`)
- String methods
  - `lower()`
  - `strip()`
- Dictionary operations
- Conditional statements
- Basic printing and formatting
- `continue`
- `break`

> **Note:** No functions, classes, modules, or external libraries are used in this project.

---

## ▶️ How to Run

1. Install Python 3.
2. Save the program as:

```
library_management.py
```

3. Open the terminal.

4. Run:

```bash
python library_management.py
```

---

## 📋 Menu

```
1. Add Book
2. Borrow Book
3. Return Book
4. Search Book
5. Display Books
6. Borrowed Book
7. Exit
```

---

## 📸 Sample Output

```
**************** Welcome To Karnataka Government Public Library ****************

1. Add Book
2. Borrow Book
3. Return Book
4. Search Book
5. Display Books
6. Borrowed Book
7. Exit

Enter Your Choice:
```

---

## 📌 Project Purpose

This project was created to practice beginner-level Python programming concepts by developing a real-world command-line application.

It demonstrates how dictionaries and loops can be used to manage data efficiently without using functions or object-oriented programming.

---

## 🔮 Future Improvements

Possible enhancements include:

- Using functions for cleaner code
- Implementing object-oriented programming (OOP)
- Adding file handling to save data permanently
- Using JSON or a database for storage
- Adding book IDs
- Tracking borrow and return dates
- Fine calculation for late returns
- User authentication
- Graphical User Interface (GUI)

\
