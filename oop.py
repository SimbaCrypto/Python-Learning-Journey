# Pytho Week 5 OOP Assignment 1

# Superhero class
class Superhero:
    def __init__(self, name, superpower, strength):
        self.name = name
        self.superpower = superpower
        self.strength = strength

    def display_hero_info(self):
        print(f"Superhero: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"Strength: {self.strength}")

    def use_power(self):
        print(f"{self.name} is using {self.superpower}!")

# Villain class inherits from Superhero
class Villain(Superhero):
    def __init__(self, name, superpower, strength, weakness):
        super().__init__(name, superpower, strength)
        self.weakness = weakness

    def display_hero_info(self):
        # Polymorphism: Overriding the method to add villain-specific info
        super().display_hero_info()
        print(f"Weakness: {self.weakness}")

    def use_power(self):
        # Villains use their powers differently than heroes
        print(f"{self.name} is using {self.superpower} for evil!")

# Create a Superhero object
hero = Superhero("Captain Amazing", "Super Strength", 100)
hero.display_hero_info()
hero.use_power()

print("\n")

# Create a Villain object
villain = Villain("Dark Lord", "Mind Control", 85, "Loud Noises")
villain.display_hero_info()
villain.use_power()
