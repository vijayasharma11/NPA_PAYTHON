import random

def practice_times_table():
    # Ask the user which times table they want to practice
    table = int(input("Which times table would you like to practice : "))
    
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    
    # Display the sum for them to guess
    print(f"What is {random_number} x {table}?")
    
    # Get the user's guess
    guess_no = int(input("Your guess: "))
    
    # Calculate the correct answer
    correct_answer = random_number * table
    
    # Check if the guess is correct
    if guess_no == correct_answer:
        print("Well done! You guessed correctly!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}. Better luck next time!")

# Run the program
practice_times_table()
