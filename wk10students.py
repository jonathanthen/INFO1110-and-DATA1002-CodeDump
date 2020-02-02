class Student:
    #global counter for ID
    sid = 0

    def __init__(self, name):
        self.name = name
        self.id = Student.sid
        Student.sid += 1

    def get_students_created():
        return Student.sid
        
students = [Student("Kerry"), Student("Xixi"), Student("Alice")]
for student in students:
    print(student.id)