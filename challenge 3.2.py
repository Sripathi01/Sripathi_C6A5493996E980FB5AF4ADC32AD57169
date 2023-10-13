
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"


def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    student_list.sort(key=lambda student: student.cgpa, reverse=True)


# Example usage:
students = [
    Student("Alice", "101", 3.8),
    Student("Bob", "102", 3.5),
    Student("Charlie", "103", 3.9),
    Student("David", "104", 3.7),
]

print("Original list of students:")
for student in students:
    print(student)

sort_students(students)

print("\nSorted list of students by CGPA (descending):")
for student in students:
    print(student)
