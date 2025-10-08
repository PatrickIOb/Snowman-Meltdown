import random
from ascii_art import STAGES
import sys

class Snowman:
    def __init__(self):
        self.mistakes = 0
        self.display_word = ""
        self.WORDS = ["python", "git", "github", "snowman", "meltdown"]
        self.secret_word = ""
        self.guessed_letters = []
        self.guess = ""

    def get_secret_word(self):
        self.secret_word = self.WORDS[random.randint(0, len(self.WORDS) - 1)]
        print(self.secret_word)

    def display_game_state(self):
        # Display the snowman stage for the current number of mistakes.
        print(STAGES[self.mistakes])
        print(self.secret_word)
        # Build a display version of the secret word.
        self.display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                self.display_word += letter + " "
            else:
                self.display_word += "_ "
        if self.display_word.replace(" ", "") == self.secret_word:
            print("Congratulations! You saved the Snowman.")
            sys.exit()
        if self.mistakes == 3:
            print("You lost! The snowman melted completely.")
            sys.exit()


        else:
            print("Word: ", self.display_word)
            print("\n")


    def play_game(self):
        self.get_secret_word()
        print("Welcome to Snowman Meltdown!")
        print("Secret word selected: " + self.secret_word)  # for testing, later remove this line

        # For now, display the initial game state.
        while self.mistakes < 4:
            self.display_game_state()


        # Prompt user for one guess (logic to be enhanced later)

            self.guess = input("Guess a letter: ").lower()
            if self.guess in self.secret_word:
                self.guessed_letters.append(self.guess)
            else:
                self.mistakes +=1




            print("You guessed:", self.guess)


if __name__ == "__main__":
    game = Snowman()
    game.play_game()