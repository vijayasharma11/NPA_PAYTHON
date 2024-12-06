# add String name varible
#name = input("Please Enter Student Name" )
#add int Score varible
#score = int(input("Please Enter Score" ))
#Display the answer 
#print()
#print(name, "has an exam score of",score) 

#Create a program that will 

#Ask user for name
userNmae = input("Please enter User name : ")
#Ask user for hours
hours = float(input("Please enter hours : "))
#Ask user for rate
rate = float(input("Please enter rate :")) 
#Calculate wages
wages = hours * rate
print ("Calculate wages : ",wages)

#Calculate tax ( wages * 20/100)
tax = (wages * 20/100) 
print("Calculate tax: ",tax)
#Display take home pay as ( wages - tax )
homePay = (wages - tax)
print("Display take home pay :", homePay)