#Ask user how many cm they want to convert to inches
#Calculate the number of inches as ( centimeters/2.54)
#Display the number of inches

#Enter the centimeter
centimeter= float(input("Please enter Centimeter : "))
#Calculate the number of inches as ( centimeters/2.54)
inches = (centimeter/2.54)
#Display the number of inches
print("The number of inches in : ",centimeter," centimeters is ", format(inches,".2f") )      