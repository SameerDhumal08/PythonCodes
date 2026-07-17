class Grandfather:
    def house(self):
        print("Grandfather's House")

class Father(Grandfather):
    def car(self):
        print("Father's Car")

class Son(Father):
    def bike(self):
        print("Son's Bike")

s = Son()

s.house()
s.car()
s.bike()
