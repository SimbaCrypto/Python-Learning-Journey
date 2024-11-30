# Python Week 5 Activity 2: Polymorphism Challenge

# Animal class
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")

# Dog class inheriting from Animals Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def move(self):
        # Dog's move action
        print(f"{self.name} the {self.breed} is running!")

# Bird class inheriting from Animal Class
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def move(self):
        # Bird's move action
        print(f"{self.name} the {self.species} is flying!")

# Vehicle class
class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        print(f"The {self.model} is moving.")

# Car class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, model, color):
        super().__init__(model)
        self.color = color

    def move(self):
        # Car's move action
        print(f"The {self.color} {self.model} is driving!")

# Plane class inheriting from Vehicle
class Plane(Vehicle):
    def __init__(self, model, airline):
        super().__init__(model)
        self.airline = airline

    def move(self):
        # Plane's move action
        print(f"The {self.airline} plane {self.model} is flying!")

# Create objects and test their move methods
dog = Dog("Buddy", "Bulldog")
dog.move()

bird = Bird("Sky", "Eagle")
bird.move()

car = Car("Tesla Model S", "Red")
car.move()

plane = Plane("Boeing 747", "American Airlines")
plane.move()
