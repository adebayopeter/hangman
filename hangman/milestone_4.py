import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Update the word_guessed to reveal the letter
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            # Reduce the number of unique letters if this was the first occurrence of the letter
            if guess not in self.list_of_guesses:
                self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break  # Exit the loop if a valid guess was made

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    game = Hangman(word_list)
    
    # Keep asking for user input until the word is guessed or lives run out
    while game.num_lives > 0 and '_' in game.word_guessed:
        print(f"Word guessed so far: {' '.join(game.word_guessed)}")
        game.ask_for_input()
        
        if game.num_letters == 0:
            print(f"Congratulations! You've guessed the word '{game.word}' correctly!")
            break
        elif game.num_lives == 0:
            print(f"Game over! The word was '{game.word}'. Better luck next time.")

