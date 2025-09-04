# Assignment 1: Design Your Own Class

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, and I protect {self.city}!")
    def save_the_day(self):
        print(f"{self.name} uses {self.power} to save {self.city}!")

# Inheritance layer
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed
    def introduce(self):
        print(f"I am {self.name}, I can fly at {self.flight_speed} km/h and my power is {self.power}!")
    def save_the_day(self):
        print(f"{self.name} flies at {self.flight_speed} km/h to save {self.city} with {self.power}!")

# Activity 2: Polymorphism Challenge
class Animal:
    def move(self):
        print("Animal moves in its own way.")

class Dog(Animal):
    def move(self):
        print("Dog runs 🐕")

class Bird(Animal):
    def move(self):
        print("Bird flies 🐦")

class Fish(Animal):
    def move(self):
        print("Fish swims 🐟")

class Vehicle:
    def move(self):
        print("Vehicle moves in its own way.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

if __name__ == "__main__":
    # Assignment 1 demo
    hero1 = Superhero("Thunderbolt", "Electric Shock", "Metro City")
    hero2 = FlyingSuperhero("Skyhawk", "Wind Blast", "Sky City", 800)
    hero1.introduce()
    hero1.save_the_day()
    hero2.introduce()
    hero2.save_the_day()

    print("\nPolymorphism Challenge:")
    animals = [Dog(), Bird(), Fish()]
    for animal in animals:
        animal.move()
    vehicles = [Car(), Plane()]
    for vehicle in vehicles:
        vehicle.move()
