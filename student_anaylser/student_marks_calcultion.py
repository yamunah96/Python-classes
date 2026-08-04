# student_data

student_data={}
#  no of students
no_of_students=int(input("Enter the number of students: "))

# loop to get student details
for i in range(no_of_students):
    print("************Kindly enter the below details*************")
    # checking for unique student name and valid input
    while True:
        student_name= input("student name: ").lower().strip()
        if student_name in student_data:
            print(f"{student_name} already exists. Please enter a different name.")
            continue
        if student_name == '':
            print("Student name cannot be empty. Please enter a valid name.")
            continue
        if not student_name.isalpha():
            print("Student name should only contain alphabetic characters. Please enter a valid name.")
            continue
        break

    # checking for valid marks input
    while True:
        maths = float(input("Math Marks (0-100): ")) 
        if 0 <= maths <= 100:
            break
        print("Enter marks between 0 and 100")
    while True:
        science = float(input("Science Marks (0-100): "))
        if 0 <= science <= 100:
            break
        print("Enter marks between 0 and 100")

    while True:
        social = float(input("Social Marks (0-100): "))
        if 0 <= social <= 100 :
            break
        print("Enter marks between 0 and 100")

    while True:
        english = float(input("English Marks (0-100): "))
        if 0 <= english <= 100:
            break
        print("Enter marks between 0 and 100")

    while True:
        kannada = float(input("Kannada Marks (0-100): "))
        if 0 <= kannada <= 100:
            break
        print("Enter marks between 0 and 100")
    marks=[maths,science,social,english,kannada]
    # total marks calculation,percentage calculation and grade calculation
    total=0
    for mark in marks:
        total+=mark
    percentage= total/5
    grade=''
    if percentage>90:
        grade='A'
    elif percentage>=80:
        grade='B'
    elif percentage>=70:
        grade='C'
    elif percentage>=60:
        grade='D'
    else:
        grade='F'

    # student data update
    student_data[student_name]={
        "total":total,"percentage":round(percentage,2),"grade":grade
    }
    print(f"{student_name} total marks: {total}, percentage: {percentage:.2f}%, grade: {grade} updated successfully")
    

highest_score=0
highest_scorer=''
lowest_score=0
lowest_scorer=''
total_percentage=0
failed_count=0

# student data analysis to find highest scorer, lowest scorer, average percentage and number of students failed
for student,data in student_data.items():
    if data['total']>highest_score:
        highest_score=data['total']
        highest_scorer=student
    if data['total']<lowest_score or lowest_score==0:
        lowest_score=data['total']
        lowest_scorer=student
    total_percentage+=data['percentage']
    if data['grade'] =="F":
        failed_count+=1

print("="*50)
print("The final Report")
print("="*50)
print("All student details:")
for student,data in student_data.items():
    print(f"{student}: Total Marks: {data['total']}, Percentage: {data['percentage']}%, Grade: {data['grade']}")

print(f"Highest Scorer: {highest_scorer} with score {highest_score}")
print(f"Lowest Scorer: {lowest_scorer} with score {lowest_score}")
print(f"Average Percentage of the class: {(total_percentage/no_of_students):.2f}%")
print(f"Number of Students who failed: {failed_count}")

    