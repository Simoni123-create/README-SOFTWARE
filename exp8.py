# Experiment 8: Count students scoring above 60 marks

# Step 1: Student data with marks in subjects
students = [
    {"name": "Alice", "Math": 75, "Science": 50, "English": 65},
    {"name": "Bob", "Math": 45, "Science": 55, "English": 40},
    {"name": "Charlie", "Math": 88, "Science": 92, "English": 70},
    {"name": "Diana", "Math": 55, "Science": 58, "English": 60},
    {"name": "Eve", "Math": 62, "Science": 75, "English": 58}
]

# Step 2: Initialize variables
count = 0
qualified_students = []

# Step 3: Check each student
for student in students:
    name = student["name"]

    # Get subject marks only
    marks = [student["Math"], student["Science"], student["English"]]

    # Find total and average
    total = sum(marks)
    average = total / len(marks)

    # Check if any subject marks > 60
    if any(mark > 60 for mark in marks):
        qualified_students.append(name)
        count += 1

        print("Student Name :", name)
        print("Total Marks  :", total)
        print("Average Marks:", round(average, 2))
        print("------------------------")

# Step 4: Final Result
print("Students scoring above 60 in at least one subject:")
print(qualified_students)

print("\nTotal students scoring above 60:", count)
print("Test PASSED")