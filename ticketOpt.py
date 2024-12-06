#Creat the menu list
print("1. Adult")
print("2. Child")
print("3. Student")
print("4. OAP")
print("5. Exit")
#Create ticke Option
ticketOption = int(input("Which option Do you select? : "))
tickets = int(input("How many tickets Do you want? :"))

if(ticketOption == 1):
    print("The cost of the tickets £", f"{tickets*19.95:.2f}")
elif(ticketOption == 2):
    print("The cost of the tickets £",f"{tickets*9.95: .2f}")
elif(ticketOption == 3):
    print("The cost of the tickets £",f"{tickets*17.95: .2f}") 
elif(ticketOption == 4):
    print("The cost of the tickets £",f"{tickets*17.95: .2f}")
else:
    print("Wrong option")       






