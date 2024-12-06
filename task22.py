# Create a program that has a string as below:

# secret="This is my secret password shhh"
# Get the length of the string secret
# Generate a random number between 1 and length of the string secret
# Ask user to guess the letter at the location of the random number selected
# IF the guess is correct print "Logged in now "
# ELSE print "You are locked out now !"


import random

# Define the secret string
secret = "This is my secret password shhh"

# Get the length of the string
length_of_secret = len(secret)

# Generate a random number between 1 and the length of the secret string
random_position = random.randint(1, length_of_secret)

# Ask the user to guess the letter at the random position (adjusted to zero-indexed)
user = input(f"Guess the letter at position {random_position} in the secret string: ")

# Check if the guess is correct
if user == secret[random_position - 1]:
    print("Logged in now")
else:
    print("You are locked out now!")
