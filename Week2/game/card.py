import random

class Card:

    def __init__(self):

        self.value = 0

    def generate(self):
    #Generates a random number between 1 and 13 
        self.value = random.randint(1, 13)