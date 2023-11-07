# import modules
import random

# Create a list containing the names of your 5 favorite fruits
favorite_fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Assign this list to a variable called word_list
word_list = favorite_fruits

# Assign the randomly generated word to a variable called word
word = random.choice(word_list)

# Ask the user to enter a single letter
guess = input("Enter a single letter: ")

# Check if the input is exactly one alphabetical character
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    # Print an error message if the input is not a single alphabetical character
    print("Oops! That is not a valid input.")

# Print out the newly created list to the standard output (screen)
# print(word)