def main():
    #Get item name
    item_name = input("Enter the item name: ")

    #Set initial cost value
    cost = 0

    # for valid cost input (must be greater than 0)
    while cost <= 0:
        cost_input = input("Enter the cost of the item (must be greater than 0): ")
        
        if cost_input.replace('.', '', 1).isdigit() and cost_input.count('.') <= 1: 
            cost = float(cost_input)
            if cost <= 0:
                print("The cost must be greater than 0. Please try again.")
        else:
            print("Invalid input. Please enter a valid number for the cost.")

    # Set initial quantity value
    quantity = 0

    # Prompt for valid quantity input (must be greater than 0)
    while quantity <= 0:
        quantity_input = input("Enter the quantity (must be greater than 0): ")
        
        if quantity_input.isdigit():
            quantity = int(quantity_input)
            if quantity <= 0:
                print("The quantity must be greater than 0. Please try again.")
        else:
            print("Invalid input. Please enter a valid positive integer for the quantity.")

    # Calculate total price
    total_price = cost * quantity

    #  Calculate delivery cost based on quantity
    if quantity > 100:
        # Free delivery
        delivery_cost = 0.00  
    elif quantity > 50:
         # Delivery cost £1.99
        delivery_cost = 1.99 
    elif quantity > 10:
        # Delivery cost £2.99
        delivery_cost = 2.99  
    else:
        # Delivery cost £4.99
        delivery_cost = 4.99  

    
    print(f"The total price for {quantity} {item_name}(s) is: £{total_price:.2f}")
    print(f"Delivery cost: £{delivery_cost:.2f}")

# Run the main program
if __name__ == "__main__":
    main()
