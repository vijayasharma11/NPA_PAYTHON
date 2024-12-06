#Create a program that will read in a first and last name,

# It will then show a menu as below and manipulate the string 

# Print in capitals
# Print in lowercase
# Print Capitalised
# Print length of string
# Print position number of the space ' ' 
# Print the string with any white space removed.
# Print the letter 0 of the first name and last name together to show a username e.g. vmclean

def main():

    first_name = input("Please Enter First Name : ")
    last_name =  input("please Enter Lat Name : ")

    #Display the Menu
    print("\n Select An Option : ")
    print("1. Print in capitals : ")
    print("2. Print in lowercase : ")
    print("3. Print Capitalised : ")
    print("4. Print length of string : ")
    print("5. Print position number of the space ' '  : ")
    print("6. Print the string with any white space removed : ")
    print("7. Print a username (first letter of first name and last name)")

    choice = int(input("\nEnter your choice(1-7): "))

    if(choice == 1):
         print(f"\nIn capitals: {first_name.upper()} {last_name.upper()}")

    elif (choice == 2):
         print(f"\nIn lowercase:{first_name.lower()} {last_name.lower()}")
    
    elif(choice == 3):
         print(f"\nIn Capitalised:{first_name.capitalize()} {last_name.capitalize()}") 
    
    elif(choice == 4):
        full_name = first_name + " " + last_name
        print(f"\nLength of the full name: {len(full_name)}")

    elif(choice == 5):
            space_position = full_name.find(' ')
            if space_position != -1:
                print(f"\nPosition of space: {space_position}")
            else:
             print("\nNo space found in the name.")
    
    elif(choice == 6):
         full_name_no_space =full_name.replace(" ","")
         print(f"\nfull name without space :{full_name_no_space}")

    elif choice == 6:
        # Print the string with any white space removed
        full_name_no_spaces = full_name.replace(" ", "")
        print(f"\nFull name without spaces: {full_name_no_spaces}")

    elif choice == 7:
        # Print the username (first letter of first and last names)
        username = first_name[0].lower() + last_name[0].lower()
        print(f"\nUsername: {username}")

    else:
        print("\nInvalid choice. Please select a number between 1 and 7.")

# Run the program
if __name__ == "__main__":
    main()