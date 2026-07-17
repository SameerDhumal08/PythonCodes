class Father:
    def money(self):
        print("Father has money")

class Mother:
    def jewelry(self):
        print("Mother has jewelry")

class Child(Father, Mother):
    pass

c = Child()

c.money()
c.jewelry()
