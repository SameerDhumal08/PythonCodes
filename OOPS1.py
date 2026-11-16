class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
       

    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)

s1 = Student("Saurabh", 34, 95)

s1.display()
