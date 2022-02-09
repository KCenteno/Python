from pet import Pet
from ninja import Ninja



class SuperPet(Pet):
    def __init__(self, first_name, type, pet_food, trick, special_move):
        super().__init__(first_name, type, pet_food, trick,)
        self.special_move = special_move

    def fight(self):
        print(f"{self.first_name} use {self.special_move}")



Solar = SuperPet("Flash", "Dog", "Sandwich", "Fight", "Solar Flare" )
moon = Pet("Moon", "dog", "hotdogs", "beg")
sun = Pet("Sun", "cat", "cake", "play dead")
star = Pet("Star", "snake", "Rats", "jump")
Kevin = Ninja("Kevin", "Rock", "Hotdogs", "Burgers", moon)
Gavin = Ninja("Gavin", "Ruby", "chips", "Chicken", sun)
Jared = Ninja("Jared", "Crystal", "pasta", "Cake", star)
Man = Ninja("Man", "Crystal", "pasta", "Cake", Solar)

Gavin.walk()
Kevin.feed()
Jared.bathe()
Man.walk()
Solar.fight()
