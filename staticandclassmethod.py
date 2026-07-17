class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def school_name(cls):
        print(cls.school)

    @staticmethod
    def greet():
        print("Welcome Students")

Student.school_name()
Student.greet()
