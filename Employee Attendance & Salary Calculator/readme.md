# Employee Payroll Management System

## Description

The **Employee Payroll Management System** is a console-based Python application that calculates employee salaries based on attendance and late arrivals. The application computes gross salary, applies deductions according to company policies, determines the final salary, and generates payroll statistics.

This project demonstrates the implementation of core Python concepts such as dictionaries, loops, conditional statements, data processing, and payroll calculations.

---

## Features

- Accepts details for multiple employees.
- Calculates gross salary based on salary per day and days present.
- Applies salary deductions according to late attendance rules.
- Calculates:
  - Gross Salary
  - Deduction Percentage
  - Deduction Amount
  - Final Salary
- Stores employee payroll records using nested dictionaries.
- Generates payroll statistics including:
  - Highest salary
  - Lowest salary
  - Highest salaried employee
  - Lowest salaried employee
  - Total company payroll

---

## Salary Deduction Rules

| Late Days | Deduction |
|-----------|----------:|
| 0 – 2 | 0% |
| 3 – 5 | 5% |
| 6 – 10 | 10% |
| Above 10 | 20% |

---

## Technologies Used

- Python 3

---

## Concepts Covered

- Variables
- Lists
- Dictionaries
- Nested Dictionaries
- Tuples
- Loops (`for`)
- Conditional Statements
- Arithmetic Operations
- Payroll Calculations
- Data Aggregation
- Finding Maximum and Minimum Values

---

## Project Structure

```text
Employee-Payroll-Management-System/
│
├── employee_payroll.py
└── README.md
```

---

## How to Run

1. Install Python 3 on your system.
2. Clone this repository or download the project files.
3. Open a terminal in the project directory.
4. Run the application using:

```bash
python employee_payroll.py
```

---

## Application Workflow

1. Enter the number of employees.
2. Enter employee details:
   - Employee Name
   - Salary Per Day
   - Days Present
   - Late Days
3. The application calculates:
   - Gross Salary
   - Deduction Percentage
   - Deduction Amount
   - Final Salary
4. Displays individual employee salary details.
5. Generates the final payroll summary.

---

## Sample Input

```text
Enter the number of employees: 2

Employee Name: Rahul
Salary Per Day: 1200
Present Days: 25
Late Days: 4

Employee Name: Priya
Salary Per Day: 1500
Present Days: 26
Late Days: 1
```

---

## Sample Output

```text
Name: Rahul
Gross Salary: ₹30000
Deduction Percentage: 5%
Deduction Amount: ₹1500
Final Salary: ₹28500

Name: Priya
Gross Salary: ₹39000
Deduction Percentage: 0%
Deduction Amount: ₹0
Final Salary: ₹39000

============================================================
Highest Salary            : ₹39000
Lowest Salary             : ₹28500
Highest Salaried Employee : Priya
Lowest Salaried Employee  : Rahul
Total Company Payroll     : ₹67500
```

---

## Data Structures Used

### Salary Deduction Rules

```python
salary_rules_data = {
    (0, 2): 0,
    (3, 5): 5,
    (6, 10): 10,
    (11, float("inf")): 20
}
```

### Employee Payroll Records

```python
employee_salary_data = {
    "Rahul": {
        "salary_per_day": 1200,
        "present_days": 25,
        "late_days": 4,
        "gross_salary": 30000,
        "deduction_percentage": 5,
        "deduction_amount": 1500,
        "final_salary": 28500
    }
}
```

---

## Payroll Calculations

### Gross Salary

```text
Gross Salary = Salary Per Day × Days Present
```

### Deduction Amount

```text
Deduction Amount = Gross Salary × (Deduction Percentage / 100)
```

### Final Salary

```text
Final Salary = Gross Salary − Deduction Amount
```

---

## Input Validation

The application currently validates:

- Number of employees should be greater than zero.

## Learning Outcomes

This project demonstrates practical knowledge of:

- Payroll system development
- Business rule implementation
- Working with nested dictionaries
- Data aggregation and reporting
- Finding maximum and minimum values
- Salary and deduction calculations
- Writing structured and maintainable Python code

Github file link: https://github.com/yamunah96/Python-classes/blob/main/Employee%20Attendance%20%26%20Salary%20Calculator/Employee_salary_calculation.py
