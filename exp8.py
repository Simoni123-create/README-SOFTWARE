# Experiment 8: Count students scoring above 60

# Step 1: Student data with marks in subjects
students = [
    {'name': 'Alice', 'Math': 75, 'Science': 50, 'English': 65},
    {'name': 'Bob', 'Math': 45, 'Science': 55, 'English': 40},
    {'name': 'Charlie', 'Math': 88, 'Science': 92, 'English': 70},
    {'name': 'Diana', 'Math': 55, 'Science': 58, 'English': 60},
    {'name': 'Eve', 'Math': 62, 'Science': 75, 'English': 58}
]

# Step 2: Initialize count
count = 0

# Step 3: Check each student
for student in students:
    name = student['name']
    
    # Get marks (excluding name)
    subjects = {k: v for k, v in student.items() if k != 'name'}
    
    # Check if any subject > 60
    if any(mark > 60 for mark in subjects.values()):
        print(name, "scored above 60")
        count += 1

# Step 4: Print result
print("\nTotal students scoring above 60:", count)
print("Test PASSED")