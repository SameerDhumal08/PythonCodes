from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @abstractmethod
    def work(self):
        pass

    def salary(self):
        return self.__salary


class Developer(Employee):

    def work(self):
        print(self.name, "develops software")


class Tester(Employee):

    def work(self):
        print(self.name, "tests software")


employees = [
    Developer("Sameer", 70000),
    Tester("Rahul", 50000)
]

for emp in employees:
    emp.work()
    print(emp.salary())
