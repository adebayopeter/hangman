import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman game with a word and a set number of lives."""
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def _update_word_guessed(self, guess):
        """Private method to update the word_guessed list based on the guess."""
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess

    def check_guess(self, guess):
        """Check the player's guess and update the game state accordingly."""
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
            if guess not in self.list_of_guesses:
                self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """Prompt the player for a letter guess and handle the input."""
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

def play_game(word_list):
    """Function to start and manage the Hangman game."""
    game = Hangman(word_list, num_lives=5)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        print(f"Word guessed so far: {' '.join(game.word_guessed)}")
        if game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    play_game(word_list)
