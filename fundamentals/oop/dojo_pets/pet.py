class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, first_name, type, pet_food, trick):
        self.first_name = first_name
        self.type = type
        self.trick = trick
        self.pet_food = pet_food
        self.health = 100
        self.energy = 100
# implement the following methods:

# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.first_name} is rally sleepy")

# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Hey {self.first_name} is going to eat {self.pet_food}")

# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"Hey {self.first_name} wants to play.")

# noise() - prints out the pet's sound
    def noise(self):
        print(f"Hey {self.first_name} is really mad.")