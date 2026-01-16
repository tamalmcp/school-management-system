class course:
    def __init__(self, title):
        self.title = title


class Student:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.__password = password


    def enroll_student(self, course_name):
        with open("students.txt", "a") as file:
            file.write(f"Name: {self.name}, Roll: {self.roll}, Course: {course_name}\n")

def show_all_students():
    with open("Students.txt", "r") as file:
        # lines = file.readlines()
        for line in file:
            print(line)


# Student = Student('Two', '2', '123456')
# Student.enroll_student('Python')

show_all_students()

