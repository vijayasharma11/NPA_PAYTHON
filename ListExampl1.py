# display the menu
print("1 : Show List ")
print("2 : Append List ")
print("3 : Insert List")
print("4 : Length of list")
print("5 : Exit")
print()

# Define the initial list
menu_list =[33,4,"Hello",3.14,"Sunshine"]
choice = 0

 # Get the user's choice
while choice != 5:
    choice = int(input("Enter your choice (1-5): "))
    
    # Handle the user's choice
    if(choice == 1):
        print("Current List: ",menu_list)

    elif(choice == 2):
        item_to_append = input("Enter the item to append : ")
        menu_list.append(item_to_append)
        print(f"{item_to_append}' has been appended to the list")

    elif(choice == 3):
        insert_list = input("Enter the list to insert :")
        menu_list.insert(1,insert_list)
        print(f"{insert_list}' has been inseted to the list ")
        
    elif( choice == 4) :
            print("Length of the list:", len(menu_list))
            
    elif (choice == 5):
            print("Exiting the program. Goodbye!")
    else:
            print("Error: Invalid choice. Please select a number between 1 and 5.")
