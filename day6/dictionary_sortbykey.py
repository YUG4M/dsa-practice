students = [
    {"name": "Yash", "marks": 78},
    {"name": "Rahul", "marks": 85},
    {"name": "Aman", "marks": 69}
]

sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)

for student in sorted_students:
    print(student)
