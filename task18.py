import random

def practice_times_table():
  
    table = int(input("Which times table would you like to practice (e.g. 2, 3, 4...): "))
    
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    
    
    correct_answer = random_number * table
    
    # Give the user up to 3 attempts to guess the correct answer
    attempts = 0
    while attempts < 3:
        
        print(f"What is {random_number} x {table}?")
        
        # Get the user's guess2
        guess_no = int(input("Your guess: "))
        
        # Check if the guess is correct
        if guess_no == correct_answer:
            print("Well done! You guessed correctly!")
            break  
        else:
            print("Incorrect.")
        
       
        attempts += 1
    
    # If all attempts are used, reveal the correct answer
    if attempts == 3 and guess_no != correct_answer:
        print(f"The correct answer is {correct_answer}. Better luck next time!")

# Run the program
practice_times_table()
