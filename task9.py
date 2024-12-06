 

# this funtion will display the menu 
def option_menu():
  print("\n Welcome to the ticketing app \n")
  print("1: Adult ticket")
  print("2: Child ticket")
  print("3: Student ticket")
  print("4: OAP avalible")
  print("5: Exit")
  return
  
# this is function will show tickets for adult
def Adult_Ticket():
  tickets = int(input("Plase enter the amount of tickets : "))
  cost = tickets* 19.95  
  print("\n the cost of ticket is = ", cost)
  return

# this function adds ticket for child
def Child_Ticket():
  tickets = int(input("Plase enter the amount of tickets : "))
  cost = tickets* 9.95  
  print("\n the cost of ticket is = ", cost)
  return

# this function adds ticket for Student
def Student_Ticket():
  tickets = int(input("Plase enter the amount of tickets : "))
  cost = tickets* 17.95  
  print("\n the cost of ticket is = ", cost)
  return
  
# this function adds ticket for OAP
def OAP_Ticket():
  tickets = int(input("Plase enter the amount of tickets : "))
  cost = tickets* 9.95  
  print("\n the cost of ticket is = ", cost)
  return

choice = 0
    
  # the password part of the program
for x in range(3):
  # we takein the user credentials
  user_name = str(input('\n please enter username= : '))
  user_pwd = str(input('\n please enter password= : '))
  
  # we check the user credentials witj tje if statement
  if (user_pwd == "pass" and user_name == "name"):
    
    print("\n welcome to the ticket site")  
    while (choice !=5):
      option_menu()
      choice = int(input("please enter the ticket choice from list \n : "))
      # we make a choice
  
      if (choice==1): Adult_Ticket()
      elif   (int(choice)==2): Child_Ticket()
      elif   (int(choice)==3): Student_Ticket()
      elif   (int(choice)==4): OAP_Ticket()
      elif   (int(choice)==5): print("Goodbye ")
      else: print("You have enterd an incorrect option")
    break   

  else:
    print("\n incorect password attempt ",x+1)


print("\n you have now exited the program - goodbye !")