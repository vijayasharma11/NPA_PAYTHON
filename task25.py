# Function to authenticate user with username and password
def authenticate_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Hardcoded username and password (You can change these)
    correct_username = "vijaya"
    correct_password = "glasgow"
    
    attempts = 3
    
    # Loop for 3 login attempts
    while attempts > 0:
        if username == correct_username and password == correct_password:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect login. You have {attempts} attempt(s) left.")
            if attempts > 0:
                username = input("Enter username: ")
                password = input("Enter password: ")
    
    print("Too many failed login attempts.")
    return False

# Function to display the menu and perform operations
def display_menu():
    wages = []
    
    while True:
        print("\n--- Menu ---")
        print("1. Read data from file")
        print("2. Calculate Wages (add to list)")
        print("3. Print Wages")
        print("4. Find Max Wage")
        print("5. Find Min Wage")
        print("6. Count Wages under £100")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            # Read data from file and store in list
            wages = read_data_from_file("wages.txt")
        elif choice == "2":
            # This functionality is already handled by the file reading, no need for extra code
            print("Wages already added from the file.")
        elif choice == "3":
            print_wages(wages)
        elif choice == "4":
            max_wage = find_max_wage(wages)
            print(f"Max wage: £{max_wage}")
        elif choice == "5":
            min_wage = find_min_wage(wages)
            print(f"Min wage: £{min_wage}")
        elif choice == "6":
            count_under_100 = count_wages_under_100(wages)
            print(f"Number of wages under £100: {count_under_100}")
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to read data from the file and return a list of wages
def read_data_from_file(file_name):
    wages = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, wage = line.split()
                wage = float(wage)
                wages.append(wage)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    return wages

# Function to print the wages list
def print_wages(wages):
    if wages:
        print("\nWages:")
        for i, wage in enumerate(wages, start=1):
            print(f"{i}. £{wage}")
    else:
        print("No wages to display.")



# Function to find the max wage
def find_max_wage(wages):
    if wages:
        return max(wages)
    else:
        return "No wages to calculate max."

# Function to find the min wage
def find_min_wage(wages):
    if wages:
        return min(wages)
    else:
        return "No wages to calculate min."

# Function to count wages under £100
def count_wages_under_100(wages):
    return len([wage for wage in wages if wage < 100])

# Main program
def main():
    # Authenticate user
    if authenticate_user():
        # Show the menu if login is successful
        display_menu()
    else:
        print("Exiting the program due to failed login attempts.")

# Run the main program
if __name__ == "__main__":
    main()
