print("Welcome to student record management system")

name = input("Enter the name:")
marks = int(input("Enter the marks:"))

if marks >=50:
    print(f"{name} has passed with {marks} marks.")
else:
    print(f"{name} has failed with {marks} marks.")



