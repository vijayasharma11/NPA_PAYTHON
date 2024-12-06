# Ask user to enter their full name e.g. Violet Mclean
# Get the Initials from the 2 names entered e.g. V M
# Use Random to find a number between 1 and 100.
# Add the number after the initials and print as a persons Username e.g. VM32

import random

# Ask the user to input their full name
full_name = input("Enter your full name (e.g., Violet Mclean): ")

# Extract initials
name_parts = full_name.split()
initials = "".join([part[0].upper() for part in name_parts])

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

#  Create the username by appending the random number to the initials
username = initials + str(random_number)

# Print the generated username
print(f"Your generated username is: {username}")
