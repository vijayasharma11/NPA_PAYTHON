# Ask the user for the type of conversion they want to perform
currency_type = input("Do you want to convert from Pounds to Euros : ? ")

# Define the conversion rates
pounds_to_euros_rate = 0.87  
euros_to_pounds_rate = 1.14  


if (currency_type == "pounds" or currency_type == "Pounds") :
        print("£1 =1.14 Euro")
        pounds = float(input("Enter the amount in Pounds to convert : "))
        euros = pounds * euros_to_pounds_rate
        print(f"{pounds} Pounds is equal to {euros:.2f} Euros.")
elif (currency_type == "euros" or currency_type == "Euros"): 
        print("1 euro = £0.87")
        euros = float(input("Enter the amount in Euros to convert: "))
        pounds = euros * pounds_to_euros_rate
        print(f"{euros} Euros is equal to {pounds:.2f} Pounds.")
else:
    print("Invalid input. Please enter 'Pounds' or 'Euros'.")
