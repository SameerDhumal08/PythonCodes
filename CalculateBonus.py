'''Create a parameterized constructor accepting:
- name
- salary
- experience

Create a method called calculate_bonus().

Calculate bonus based on experience:
- Experience greater than or equal to 5 years → 20% bonus.
- Experience less than 5 years → 10% bonus.

Create a method called display_details() to print employee details and total salary.'''

class Employee:
    
    def __init__(self,name, salary, experiance):
        self.name = name
        self.salary = salary
        self.experiance = experiance
 
    def calculate_bonus(self):
        if self.experiance >= 5:
            self.salary = self.salary + self.salary * (20/100)
        else:
            self.salary = self.salary + self.salary * (10/100)
    
    def display_details(self):
        print("Employee : ",self.name)
        print("Total Salary : ",self.salary)
    
E1 = Employee("Sameer",20000,2)
E1.calculate_bonus()
E1.display_details()

E2 = Employee("Sam",20000,5)
E2.calculate_bonus()
E2.display_details()

E3 = Employee("Sameer",20000,6)
E3.calculate_bonus()
E3.display_details()
