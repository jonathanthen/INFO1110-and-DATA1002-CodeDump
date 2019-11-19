students = int(input("Enter the number of students in the class: "))

for n in range(1, students+1):
  mark = int(input("Enter student mark: "))
  
  if mark >= 45:
    print("Pass")
  else:
    print("Fail")