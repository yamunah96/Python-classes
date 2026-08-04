'''
Description
A company has multiple employees.
For each employee:
Input: Name, Salary per day, Days Present,Late Days

Rules: Late deductions:
0-2 late-   No deduction
3-5 late-  5% deduction
6-10 late- 10% deduction
Above 10- 20% deduction

Display
Gross Salary, Deduction, Final Salary
Highest salary, Lowest salary, Total company payroll, Employee earning maximum salary
'''

print("**************ABC private limited******************")

# rules dict
salary_rules_data={
    (0,2):0,
    (3,5):5,
    (6,10):10,
    (11,float('inf')):20
}

# employee data dict
employee_salary_data={}

# employes number
employee_number= int(input("Enter the number of employees: "))

# checking employee number not less than or equal to zero
if employee_number <=0:
    print("Employee number should be greater than 0")
    exit()

# enter the number of employees details
for i in range(employee_number):
    employee_name= input("Enter the employee name: ")
    salary_per_day= float(input("Enter the employee salary per day: "))
    present_days= int(input("Enter the Present Days: "))
    late_days=int(input("Enter the late Days: "))

    # Gross salary calculation
    gross_salary= salary_per_day* present_days
    deduction=0

    #checking percentage for deduction amount calculation
    for (minimum,maximum),percentage in salary_rules_data.items():
        if minimum <= late_days <= maximum:
            deduction= percentage

    # deduction amount
    deduction_amount= gross_salary* (percentage/100)
    # final Salary 
    final_salary= gross_salary-deduction_amount

    print(f"Name: {employee_name}\nSalary_per_day: ₹{salary_per_day}\nPresent_day: {present_days}\nLate Days: {late_days}\nGross Salary: ₹{gross_salary}\nDeduction_percentage: {deduction}%\nDeduction Amount:₹{deduction_amount}\nFinal Salary: ₹{final_salary}")
    print(" ")

    # storing the each employee info in employee_salary_data dict
    employee_salary_data[employee_name]={
        "salary_per_day":salary_per_day,
        "present_days":present_days,
        "late_days":late_days,
        "gross_salary":gross_salary,
        "deduction_percentage":deduction,
        "deduction_amount":deduction_amount,
        "final_salary":final_salary
    }
print("="*100)
print(employee_salary_data)

salary_list=[]
total_pay=0
# calculating total pay roll and highest  and lowest salary
for employee_name, data in employee_salary_data.items():
    salary_list.append((employee_name,data['final_salary']))
    total_pay+=data['final_salary']
print(salary_list)

# [('y', 1600.0), ('r', 1600.0)]
highest_salary= max(salary for name, salary in salary_list)
lowest_salary= min(salary for name, salary in salary_list)

# Highest and Slowest Salaried Employee
highest_salaried_employee=""
lowest_salaried_employee=""
for name, salary in salary_list:
    if salary == highest_salary:
        highest_salaried_employee=name
    if salary == lowest_salary:
        lowest_salaried_employee=name


print("Highest salary", highest_salary)
print("Lowest salary", lowest_salary)
print("Highest Salaried Employee", highest_salaried_employee)
print("Lowest Salaried Employee", lowest_salaried_employee)
print("Total PayRoll", total_pay)


