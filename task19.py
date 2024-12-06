# Function to display the menu
def display_menu():
    print("1: Show List")
    print("2: Add Week's Temperatures")
    print("3: Show Average Temp")
    print("4: Show Max Temp")
    print("5: Exit Program")

# Function to show the list of temperatures
def show_list(temps):
    if temps:  
        print("Temperatures for the week:", temps)
    else:
        print("No temperatures recorded yet.")

# Function to add temperatures for the week 
def add_temperatures():
    temperatures = []
    print("Please enter the temperatures for the next 7 days:")
    for i in range(1, 8):
        valid_input = False
        while not valid_input:
            temp_input = input(f"Enter temperature for day {i}: ")
            
            if temp_input.replace('.', '', 1).isdigit() and temp_input.count('.') <= 1:
                temp = float(temp_input)
                temperatures.append(temp)
                valid_input = True 
            else:
                print("Invalid input! Please enter a valid number for the temperature.")
    return temperatures

# Function to calculate the average temperature
def show_average_temp(temps):
    if temps:
        avg_temp = sum(temps) / len(temps)
        print(f"The average temperature for the week is: {avg_temp:.2f}°C")
    else:
        print("No temperatures recorded to calculate the average.")

# Function to find the maximum temperature
def show_max_temp(temps):
    if temps:
        max_temp = max(temps)
        print(f"The highest temperature for the week is: {max_temp}°C")
    else:
        print("No temperatures recorded to find the max temperature.")

# Main function to run the program
def main():
    temperatures = []  
    choice = 0 
    while choice != 5:
        display_menu()  
        choice_input = input("Enter your choice: ")  
        
        
        if choice_input.isdigit():
            choice = int(choice_input)
        else:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue 

        if choice == 1:
            show_list(temperatures)  
        elif choice == 2:
            temperatures = add_temperatures()  
        elif choice == 3:
            show_average_temp(temperatures)  
        elif choice == 4:
            show_max_temp(temperatures)  
        elif choice == 5:
            print("Exiting the program. Goodbye!") 
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")  

# Run the main program
if __name__ == "__main__":
    main()
