# Define the initial list
info_list = [33, 4, "Hello", 3.14, "Sunshine"]

choice = 0

while choice != 5:
    # Show the menu
    print("\nMenu:")
    print("1: Show List")
    print("2: Append to List")
    print("3: Insert into List")
    print("4: Display Length of List")
    print("5: Exit Program")
    
    # Get the user's choice
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue
    
    # Handle the user's choice
    if choice == 1:
        print("Current List:", info_list)
        
    elif choice == 2:
        item = input("Enter the item to append: ")
        info_list.append(item)
        print(f"'{item}' has been appended to the list.")
        
    elif choice == 3:
        try:
            index = int(input("Enter the index to insert at: "))
            item = input("Enter the item to insert: ")
            if index < 0 or index > len(info_list):
                print("Error: Index out of range.")
            else:
                info_list.insert(index, item)
                print(f"'{item}' has been inserted at index {index}.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
            
    elif choice == 4:
        print("Length of the list:", len(info_list))
        
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        
    else:
        print("Error: Invalid choice. Please select a number between 1 and 5.")
