# Dictionary to store grades
grades = {}

def assign_grade(student_id, grade_type, grade_value):
    # Only store non-zero grades
    if grade_value != 0:
        if student_id not in grades:
            grades[student_id] = {}
        grades[student_id][grade_type] = grade_value

def display_grades():
    # Display grades for all students
    if not grades:
        print("No grades to display.")
    else:
        for student_id, student_grades in grades.items():
            print(f"Student {student_id}:")
            for grade_type, grade_value in student_grades.items():
                print(f"  {grade_type}: {grade_value}")
            print()

# Input loop to get data from the user
while True:
    try:
        student_id = int(input("Enter student ID (or -1 to stop): "))
        
        if student_id == -1:
            break  # Exit the loop if user enters -1 to stop

        grade_type = input("Enter grade type (e.g., 'assignment1', 'quiz1'): ")
        
        if not grade_type.strip():  # Make sure the grade type is not empty
            print("Grade type cannot be empty. Please try again.")
            continue
        
        grade_value = float(input(f"Enter grade for {grade_type}: "))

        if grade_value < 0 or grade_value > 100:  # Validating grade range
            print("Please enter a valid grade between 0 and 100.")
            continue

        # Assign the grade
        assign_grade(student_id, grade_type, grade_value)

    except ValueError:
        print("Invalid input. Please enter valid numbers for student ID and grade.")

# Display all grades
display_grades()
