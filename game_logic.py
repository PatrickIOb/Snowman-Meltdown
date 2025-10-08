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
        # print(self.secret_word)  # You can uncomment for testing

    def display_game_state(self):
        # Clear and structured game display
        print("\n" + "-" * 40)
        print(STAGES[self.mistakes])
        print("-" * 40)

        # Build a display version of the secret word
        self.display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                self.display_word += letter + " "
            else:
                self.display_word += "_ "

        print("Word:", self.display_word)
        print("Guessed letters:", " ".join(self.guessed_letters))
        print(f"Mistakes: {self.mistakes}/{len(STAGES) - 1}")

        # Win condition
        if self.display_word.replace(" ", "") == self.secret_word:
            print("\n🎉 Congratulations! You saved the Snowman.")
            self.play_again()  # Ask to replay
            return

        # Lose condition
        if self.mistakes == len(STAGES) - 1:
            print("\n💧 You lost! The snowman melted completely.")
            print("The word was:", self.secret_word)
            self.play_again()
            return

    def get_valid_guess(self):
        # Input validation for a single alphabetical character
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("❌ Please enter only one letter (a-z).")
            elif guess in self.guessed_letters:
                print("⚠️ You already guessed that letter.")
            else:
                return guess

    def play_again(self):
        # Replay option
        again = input("\nWould you like to play again? (y/n): ").lower()
        if again == "y":
            self.__init__()   # Reset the game state
            self.play_game()
        else:
            print("👋 Thanks for playing Snowman Meltdown!")
            sys.exit()

    def play_game(self):
        self.get_secret_word()
        print("\nWelcome to Snowman Meltdown!")
        print("Try to guess the secret word before the snowman melts!\n")

        # Main gameplay loop
        while self.mistakes < len(STAGES):
            self.display_game_state()

            # Break out if game ended (won or lost)
            if self.display_word.replace(" ", "") == self.secret_word or self.mistakes == len(STAGES) - 1:
                break

            # Get and process a valid guess
            self.guess = self.get_valid_guess()

            if self.guess in self.secret_word:
                print(f"✅ Good guess! '{self.guess}' is in the word.")
                self.guessed_letters.append(self.guess)
            else:
                print(f"💧 Sorry! '{self.guess}' is not in the word.")
                self.guessed_letters.append(self.guess)
                self.mistakes += 1

if __name__ == "__main__":
    game = Snowman()
    game.play_game()
