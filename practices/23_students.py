grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongbob": "C",
          "Partick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")
