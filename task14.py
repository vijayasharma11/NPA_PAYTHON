# Function to get the name of the user
def get_name():
    name = input("Please enter user name: ")
    return name

# Function to get the age of the user
def get_age():
    age = int(input("Please enter user age: "))
    return age

# Main program to implement the algorithm
def main():
    # Get user name and age
    name = get_name()
    age = get_age()
    
    # Check if age is greater than or equal to 18
    if age >= 18:
        print(f"Welcome, {name}!")
    else:
        print(f"Sorry, {name}, you are too young.")

# Run the program
if __name__ == "__main__":
    main()
