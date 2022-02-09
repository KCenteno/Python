class Ninja:
    def __init__( self, first_name , last_name , treats , pet_food, Pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet
# implement the following methods:

# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f"Hey {self.pet.first_name} lets go on a walk.")
        self.pet.play()

# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f"{self.pet.first_name} is hungry for {self.treats}.")
        self.pet.eat()

# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"Hey {self.pet.first_name} needs a bath.")
        self.pet.noise()