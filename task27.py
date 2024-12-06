# Define the wages for each month
wages = [967, 967, 1000, 1000, 650, 1100, 1000, 1250, 967, 1000, 1200, 650]

# Function to calculate total earnings
def calculate_earnings(month):
    
    if 1 <= month <= 12:
        total_earnings = sum(wages[:month])  # Sum all wages 
        return total_earnings
    else:
        return None  # Return None for invalid month

# Ask the user for the month
month_input = int(input("Enter the month as an integer (1 for January, 12 for December): "))


total = calculate_earnings(month_input)

# Display the result
if total is not None:
    print(f"Total earnings for the year up to the end of month {month_input}: {total}")
else:
    print("Invalid month entered. Please enter a value between 1 and 12.")
