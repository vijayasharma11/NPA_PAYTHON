# Function to read data from files
def read_data():
    # lists to store items, costs, and quantities
    items = []
    costs = []
    quantities = []

    # Read data from 'items.txt'
    with open('items.txt') as f:
        items = [line.strip() for line in f.readlines()]

    # Read data from 'costs.txt'
    with open('costs.txt') as f:
        costs = [float(line.strip()) for line in f.readlines()]

    # Read data from 'quantities.txt'
    with open('quantities.txt') as f:
        quantities = [int(line.strip()) for line in f.readlines()]

    return items, costs, quantities

# Function to show total value of stock in £
def total_stock_value(costs, quantities):
    total_value = sum(cost * quantity for cost, quantity in zip(costs, quantities))
    print(f"Total value of stock: £{total_value:.2f}")

# Function to show all stock items and their quantities
def show_all_stock(items, quantities):
    print("Stock Items and Quantities:")
    for item, quantity in zip(items, quantities):
        print(f"{item}: {quantity} in stock")

# Function to show stock items with less than 30 in stock
def show_low_stock(items, quantities):
    print("Items with less than 30 in stock:")
    for item, quantity in zip(items, quantities):
        if quantity < 30:
            print(f"{item}: {quantity} in stock")

# Function to show the average stock price
def average_stock_price(costs):
    if costs:
        average = sum(costs) / len(costs)
        print(f"Average stock price: £{average:.2f}")
    else:
        print("No items to calculate average price.")

# Function to show the maximum stock price
def max_stock_price(costs):
    if costs:
        max_price = max(costs)
        print(f"Maximum stock price: £{max_price:.2f}")
    else:
        print("No items to calculate maximum price.")

# Main function to control the flow of the program
def main():
    # Read data from files
    items, costs, quantities = read_data()

    if not items:  # If there are no items, exit the program early
        print("No data available. Exiting.")
        return

    while True:
        # Display the menu
        print("\nMenu:")
        print("1. Show total value of stock in £")
        print("2. Show all current stock items and quantity")
        print("3. Show stock items with less than 30 in stock")
        print("4. Show the average stock price")
        print("5. Show the maximum stock price")
        print("6. Exit")

        # Get user choice
        choice = input("Please enter your choice (1-6): ").strip()

        if choice == '1':
            total_stock_value(costs, quantities)
        elif choice == '2':
            show_all_stock(items, quantities)
        elif choice == '3':
            show_low_stock(items, quantities)
        elif choice == '4':
            average_stock_price(costs)
        elif choice == '5':
            max_stock_price(costs)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.")

# Run the main function
if __name__ == "__main__":
    main()
