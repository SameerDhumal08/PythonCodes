class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

def animal_sound(animal):
    animal.sound()

animal_sound(Cat())
animal_sound(Cow())
