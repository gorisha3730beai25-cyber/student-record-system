from student import Student
print("Welcome to student record management system")
name = input("Enter the name:")
marks = int(input("Enter the marks:"))
student = Student(name,marks)
result = student.result()
print(f"{name} has {result} with {marks} marks.")
