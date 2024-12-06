# Define the Balance
balance = 2500


payments = [160, 160, 150, 150, 150, 150, 160, 155, 150, 160, 150, 150]

# Function to calculate total payments
def calculate_payments(month):
    if 1 <= month <= 12:
        return sum(payments[:month]) 
    else:
        return None  

# Ask the user for the month
month_input = input("Enter the month as an integer (1 for January, 12 for December): ")

# Check if the input is a valid integer and within the valid month range
if month_input.isdigit():
    month_input = int(month_input) 
    
    if 1 <= month_input <= 12:
        # Calculate the total payments up to the entered month
        total_payments = calculate_payments(month_input)
        
        # Calculate the settlement figure
        settlement = balance - total_payments
        print(f"Total payments up to month {month_input}: {total_payments}")
        print(f"Settlement figure: {settlement}")
    else:
        print("Invalid month entered. Please enter a value between 1 and 12.")
else:
    print("Invalid input. Please enter an integer for the month.")
