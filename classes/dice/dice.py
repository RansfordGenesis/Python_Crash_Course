from random import randint

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides
        
    def roll_dice(self):
        return randint(1, self.sides)
    
    def number_rolls(self, n = 10):
        for i in range(n):
            print(self.roll_dice())