def calculate_adult():
    tickets = int(input("Plase enter the amount of tickets :, "))
    cost = tickets* 19.95  
    print("\n the cost of ticket is = " ,cost)
    return

def calculate_child():
    tickets = int(input("Plase enter the amount of tickets : "))
    cost = tickets* 9.95  
    print("\n the cost of ticket is = ", cost)
    return

def calculate_student():
    print("Calculating student ticket price...")
    tickets = int(input("Plase enter the amount of tickets : "))
    cost = tickets* 17.95  
    print("\n the cost of ticket is = ", cost)
    return

def calculate_oap():
    tickets = int(input("Plase enter the amount of tickets : "))
    cost = tickets* 9.95  
    print(" the cost of ticket is = ", cost)
    return

def display_menu():
    print("\nTicketing Menu:")
    print("1. Calculate Adult Ticket")
    print("2. Calculate Child Ticket")
    print("3. Calculate Student Ticket")
    print("4. Calculate OAP Ticket")
    print("5 . Type 'exit' to quit.")
    return



choice = 0  

 # the password part of the program
for x in range(3):
  # we takein the user credentials
  user_name = input('\n please enter username= : ')
  user_pwd = input('\n please enter password= : ')
  
  # we check the user credentials witj tje if statement
  if (user_name == "vijaya" and user_pwd == "glasgow"):
    
    print("\n welcome to the ticket site")  
    while (choice !=5):
        display_menu()
        ticket = int(input("please enter the ticket choice from list : "))
        # we make a choice
        
        if (ticket == 1):
             calculate_adult()

        elif (ticket == 2):
            calculate_child()

        elif (ticket == 3):
            calculate_student()

        elif (ticket == 4):
                calculate_oap()

        elif (choice == 5): 
                print("Goodbye ")
        else: 
            print("You have enterd an incorrect option")
        break   

  else:
    print("\n incorect password attempt ",x+1)


print("\n you have now excited the program - goodbye !")


        