
import getpass
# imprt getpass module
usr=input("Username : ")
pwd=getpass.getpass()
# store the users password entered in pwd
if (usr=="vijaya") and (pwd=="secret"):
  # if login details correct we do this
  print("Welcome to ticket service")
  print("1. Adult")
  print("2. Child  ")
  print("3. Student ")
  print("4. OAP ")
  print("5. Exit ")
  # get users selection
  ticketOption = int(input("Which option Do you select? : "))
  tickets = int(input("How many tickets Do you want? :"))
  
  if (ticketOption == 1):
        print("The cost of the tickets £", f"{tickets*19.95:.2f}")

  elif (ticketOption == 2):
        print("The cost of the tickets £",f"{tickets*9.95: .2f}")

  elif (ticketOption == 3):
       print("The cost of the tickets £",f"{tickets*17.95: .2f}")

  elif (ticketOption == 4):
        print("The cost of the tickets £",f"{tickets*17.95: .2f}")
  else:
    print("Incorrect option ")
else:
  # if login details incorrect 
  print("Wrong login details, goodbye !")