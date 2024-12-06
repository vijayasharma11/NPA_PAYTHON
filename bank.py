import os

balance = 1000
overdraft  = 0

choice = 0

while(choice != 0) :
    print("Welcome to bank Application : ")
    print()
    print("1 : Display Balance ")
    print("2 : Add fund ")
    print("3 : Withdraw fund ")
    print("4 : Overdraft avaible ")
    print("5 : Exit ")
    print()

choice = int(input(" Please choice option 1 - 5 :"))
print()

if(choice == 1):
    print()
    print("YOur balance is £", balance)
elif(choice == 2):
    print()
    add = float(input("Please Enter deposite amount : "))
    balance = balance + add
    print("Your balance is £", balance)
elif(choice == 3):
    print()
    sub = float(input("Please Enter withdraw amount : "))
    balance = balance- sub
    print("Your balance is £",balance)
    # Check if there are sufficient funds
    if sub <= balance :
        balance -= sub
        print("Withdrawal successful. Your new balance is £", balance)
    else :
         print("Insufficient funds. Your current balance is £", balance)
elif(choice == 4):
    print("Your overdraft amount £", overdraft)
elif(choice == 5):
          print("Goodbye")
else :
    print("You have entered awrong choice")

#input("Please Enter key to continue")
#os.system('Cls')
        

