#Display Menu
choice = int(input("Please choose an option (1-5): "))
print("Currency Conversion Menu:")
print("1. Convert Pounds to Dollars (£1 = 0.99)")
print("2. Convert Pounds to Euro (£1 = 1.14)")
print("3. Convert Pounds to Yaun (£1 = 7.05)")
print("4. Convert Pounds to Mexican Peso (£1 = 19.86)")
print("5. Exit")

#Create a currency rates
pound_to_dollars_rates =0.99 
pound_to_euro_rates = 1.14 
pound_to_yaun_rates = 7.05
pound_to_mexicanPeso_rates = 19.86


currency_type = input("Do you want to convert from Pounds to Dollars or Euros or Yaun or Mexcian Peso : ? ")
#Loop
if (currency_type == "Dollars" or currency_type == "dollars") :
        print("£1 =$0.99")
        dollars = float(input("Enter the amount in Pounds to convert : "))
        pound = dollars * pound_to_dollars_rates
        print(f"{dollars} Pounds is equal to {pound:.2f} Dollars.")
elif (currency_type == "euros" or currency_type == "Euros") :
       print("£1 =1.14 euros")
       euros = float(input("Enter the amount to convert Euros : "))
       pound = euros * pound_to_euro_rates
       print(f"{euros} Pounds is eual to {pound:.2f} Euros. ")
elif (currency_type == "Yaun" or currency_type == "yaun") :
       print("£1 =7.05 Yaun")
       yaun = float(input("Enter the amount to convert Yaun : "))
       pound = yaun * pound_to_yaun_rates
       print(f"{yaun} Pounds is equal to {pound:.2f} Yaun.")
elif (currency_type == "Mexican Peso" or currency_type == "mexican peso") :   
       print("£1 =19.86") 
       MexicanPeso = float(input("Enter the amount to convert MaxicanPeso : "))
       pound = MexicanPeso * pound_to_mexicanPeso_rates
       print(f"{MexicanPeso} Pounds is equal to {pound:.2f} MexicanPeso.")
else:
    print("Invalid input. Please enter 'Pounds' or 'Euros' or 'Yaun' or 'Maxican Peso' .")
