import pandas as pd

# Step 1: Create student data (same idea as PDF but simpler)
students = [
    [1, "Aarav Sharma", 20, "Maths", 92],
    [2, "Bhavna Patel", 20, "Physics", 85],
    [3, "Chetan Kumar", 21, "Chemistry", 78],
    [4, "Deepa Singh", 20, "Biology", 88],
    [5, "Esha Verma", 21, "English", 91],
    [6, "Faisal Ahmed", 20, "History", 75],
    [7, "Gitika Mishra", 20, "Geography", 82],
    [8, "Harsh Gupta", 21, "Computer", 95],
    [9, "Ishita Das", 20, "Economics", 87],
    [10, "Jaya Reddy", 20, "Statistics", 79]
]

# Step 2: Create DataFrame (table)
columns = ["Roll No", "Name", "Age", "Subject", "Marks"]
df = pd.DataFrame(students, columns=columns)

# Step 3: Add Grade column (extra logic - good for marks)
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    else:
        return "C"

df["Grade"] = df["Marks"].apply(get_grade)

# Step 4: Save to Excel file
file_name = "student_records.xlsx"
df.to_excel(file_name, index=False)

# Step 5: Display output
print("Excel file created successfully!")
print("\nStudent Records:\n")
print(df)
print("Total records:", len(df))
