from game.card import Card

class Director:

    def __init__(self):
        # Initializes all the values
        self.card = 0
        self.second_card = 0
        self.is_playing = True
        self.initial_score = 300
        self.player_guess = ""

        self.card = Card()
        self.second_card = Card()

    def start_game(self):
        #Starts game 
        while self.is_playing:
            self.inputs()
            self.updates()
            self.outputs()

    def inputs(self):

        if (self.card.value == 0):
            self.card.generate()

        print(f"The first card is: {self.card.value}")
        self.player_guess = input("The next number is higher or lower? [H/L] ")
        if self.player_guess.capitalize() == "H" or self.player_guess.capitalize() == "L":
            self.second_card.generate()
            print(f"The second card is: {self.second_card.value}") 
        else:
            print("\nPlease select a correct letter")
            self.inputs()
       
    def updates(self):

        if (self.player_guess.capitalize() == "H"):
            if (self.card.value < self.second_card.value):
                self.initial_score += 100
            elif (self.card.value == self.second_card.value):
                self.initial_score += 0
            else:
                self.initial_score -= 75
        elif (self.player_guess.capitalize() == "L"):
            if (self.card.value > self.second_card.value):
                self.initial_score += 100
            elif (self.card.value == self.second_card.value):
                self.initial_score += 0
            else:
                self.initial_score -= 75

        self.card.value = self.second_card.value

        if self.initial_score <= 0:
            self.is_playing = False
            print("GAME OVER. YOU LOSE")

    def outputs(self):

        if not self.is_playing:
            return
               
        print(f"Your score is: {self.initial_score}")
        continue_playing = input("Do want to continue playing again? [Y/N] ")
        print("\n")
        if continue_playing.capitalize() == "N":
            self.is_playing = False
            print("Thanks for playing Hilo by Nadia. Hope you come back soon :)")
        elif continue_playing.capitalize() == "Y":
            self.is_playing = True
        else:
            print("Select a correct letter\n")
            self.outputs()