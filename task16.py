import random

def times_table_game():
    # Ask user which times table they want to practice
    print("Welcome to the Times Table Practice Game!")
    table = int(input("Which times table do you want to practice? (e.g., 2, 3, 4, ..., 10): "))
    
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    
    # Calculate the correct answer
    correct_answer = random_number * table
    
    # Display the sum (e.g., random_number x table)
    print(f"What is {random_number} x {table}?")
    
    # Allow the user up to 3 attempts to guess the correct answer
    attempts = 3
    for attempt in range(1, attempts + 1):
        # Get user's guess
        guess = int(input(f"Attempt {attempt} - Your guess: "))
        
        # Check if the guess is correct
        if guess == correct_answer:
            print("Well done! That's the correct answer!")
            break
        else:
            if attempt < attempts:
                print("Incorrect. Try again!")
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.")
    
# Call the function to start the game
times_table_game()
