# Function to get user information based on the option provided
def get_info(option):
    info = input(f"Please enter your {option}: ")
    return info

# Main program to implement the algorithm
def main():
    # Get user name, age, and address using GetInfo function
    name = get_info("name")
    age = int(get_info("age"))  
    address = get_info("address")
    
    # Check if age is 21 or over
    if age >= 21:
        print(f"Welcome, {name}!")
        print(f"Your address is: {address}")
    else:
        print(f"Sorry, {name}, you are too young.")

# Run the program
if __name__ == "__main__":
    main()
