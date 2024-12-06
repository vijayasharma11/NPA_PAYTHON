# Function to displaylist
def display_list(marks):
    print("Full List: ", marks)

# Function to find highest value in the list
def find_highest_value(marks):
    return max(marks)

# Function to find lowest value in the list
def find_lowest_value(marks):
    return min(marks)

# Function to count the number of values under 50
def count_under_50(marks):
    return len([value for value in marks if value < 50])

# Function to add a new value to the list after checking if it is within the valid range
def add_value(marks):
    value = input("Enter a value to add (between 0 and 100): ")
    if value.isdigit():  # Check if the input is a valid number
        value = int(value)
        if value < 0 or value > 100:
            print("Error: Value out of range!")
        else:
            marks.append(value)
            print(f"Value {value} added to the list.")
    else:
        print("Error: Please enter a valid integer.")

# Main function 
def main():
    
    marks = [20, 78, 50, 52, 12, 34, 88, 90, 3, 52]

    while True:
        # Display menu
        print("\nMenu:")
        print("1. Display List")
        print("2. Find Highest Value")
        print("3. Find Lowest Value")
        print("4. Count number of values under 50")
        print("5. Add Value")
        print("6. Exit")
        
        # Get user choice
        
        choice = int(input("Enter your choice (1-6): "))
            
        if choice == 1:
                
                display_list(marks)
                
        elif choice == 2:
                highest_value = find_highest_value(marks)
                print(f"The highest value in the list is: {highest_value}")
                
        elif choice == 3:
                lowest_value = find_lowest_value(marks)
                print(f"The lowest value in the list is: {lowest_value}")
                
        elif choice == 4:
                count = count_under_50(marks)
                print(f"The number of values under 50 is: {count}")
                
        elif choice == 5:
                add_value(marks)
                
        elif choice == 6:
                print("Exiting the program. Goodbye!")
                break
                
        else:
                print("Error: Invalid choice. Please enter a valid option (1-6).")
        
       
            

# Call the main function to start the program
if __name__ == "__main__":
    main()