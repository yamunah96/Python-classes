# Student Performance Management System

## Overview

The Student Performance Management System is a console-based Python application that allows users to manage and analyze student academic records. The application accepts details of multiple students, validates user input, calculates academic performance, and generates a summary report.

This project demonstrates the use of Python fundamentals such as dictionaries, loops, conditional statements, input validation, and basic data analysis.

---

## Features

- Accepts details for multiple students.
- Validates student names.
  - Name cannot be empty.
  - Name must contain only alphabetic characters.
  - Duplicate student names are not allowed.
- Validates marks for each subject.
  - Marks must be between 0 and 100.
- Calculates:
  - Total marks
  - Percentage
  - Grade
- Assigns grades based on percentage.
- Stores student records using a nested dictionary.
- Generates a final report including:
  - Highest scorer
  - Lowest scorer
  - Average class percentage
  - Number of students who failed

---

## Technologies Used

- Python 3

---

## Concepts Covered

- Variables
- Lists
- Dictionaries
- Nested Dictionaries
- Loops (`for`, `while`)
- Conditional Statements (`if`, `elif`, `else`)
- Input Validation
- String Methods
- Mathematical Calculations
- Data Aggregation

---

## Grade Criteria

| Percentage | Grade |
|------------|-------|
| Above 90   | A |
| 80 - 90    | B |
| 70 - 79    | C |
| 60 - 69    | D |
| Below 60   | F |

---

## Project Structure

```text
Student-Performance-System/
│
├── student_management.py
└── README.md
```

---

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run the program.

```bash
python student_management.py
```

---

## Sample Input

```text
Enter the number of students: 2

Student Name: Rahul

Math Marks: 90
Science Marks: 85
Social Marks: 78
English Marks: 88
Kannada Marks: 92

Student Name: Priya

Math Marks: 75
Science Marks: 68
Social Marks: 81
English Marks: 79
Kannada Marks: 84
```

---

## Sample Output

```text
==================================================
The Final Report
==================================================
Highest Scorer: rahul with score 433
Lowest Scorer: priya with score 387
Average Percentage of the class: 82.00%
Number of Students who failed: 0
```

---

## Data Structure Used

Each student's information is stored as a nested dictionary.

```python
student_data = {
    "rahul": {
        "total": 433,
        "percentage": 86.6,
        "grade": "B"
    }
}
```

---

## Future Improvements

- Store subject-wise marks in the dictionary.
- Display complete details of every student in the final report.
- Add exception handling for invalid numeric input.
- Save student records to a CSV or JSON file.
- Implement a menu-driven interface.
- Add options to search, update, and delete student records.
- Generate detailed performance statistics.

---

## Learning Outcomes

This project provides practical experience with:

- Building console-based applications
- Organizing data using dictionaries
- Implementing input validation
- Performing calculations and data analysis
- Writing clean and modular Python code

video: https://youtu.be/GIc38bCIZxI
