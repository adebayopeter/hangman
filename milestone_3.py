import random

# List of words to choose from
word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Choosing a random word from the list as the secret word
secret_word = random.choice(word_list)

def check_guess(guess):
    """Check if the guessed letter is in the secret word."""
    # Step 2: Convert the guess into lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        
def ask_for_input():
    """Ask the user for their guess and check it."""
    while True:
        # Step 2: Get user input for a guess
        guess = input("Guess a letter: ")

        # Step 3: Check if input is a valid guess
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call the check_guess function
            check_guess(guess)
            break  # Break after a valid attempt (you can remove this if you need continuous guessing)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()





