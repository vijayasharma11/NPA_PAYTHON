def main():
    # Get item name
    item_name = input("Enter the item name: ")

   # Set initial cost value
    cost = 0

    #  for valid cost input (must be greater than 0)
    while cost <= 0:
        cost_input = input("Enter the cost of the item (must be greater than 0): ")
        
        if cost_input.replace('.', '', 1).isdigit() and cost_input.count('.') <= 1: 
            cost = float(cost_input)
            if cost <= 0:
                print("The cost must be greater than 0. Please try again.")
        else:
            print("Invalid input. Please enter a valid number for the cost.")

    #  Set initial quantity value
    quantity = 0

    # Step 5: Prompt for valid quantity input (must be greater than 0)
    while quantity <= 0:
        quantity_input = input("Enter the quantity (must be greater than 0): ")
        # Check if the input is a valid positive integer
        if quantity_input.isdigit():
            quantity = int(quantity_input)
            if quantity <= 0:
                print("The quantity must be greater than 0. Please try again.")
        else:
            print("Invalid input. Please enter a valid positive integer for the quantity.")

    # Calculate total price
    total_price = cost * quantity

    # Output the total price and item name
    print(f"The total price for {quantity} {item_name}(s) is: ${total_price:.2f}")

# Run the main program
if __name__ == "__main__":
    main()

