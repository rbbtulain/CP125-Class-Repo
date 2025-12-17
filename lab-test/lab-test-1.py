# Programmer's Name: Ain
# Write a Python program that checks the grade for one student.

def determine_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"


# Main program
mark = int(input("Enter the student's mark: "))

grade = determine_grade(mark)

print("Student's mark:", mark)
print("Student's grade:", grade)
