

1.Ask user what type of pet
2.Get pet type
3.If condition pet is a dog or pet is a cat
    print insurance is£10
5.else
  print insurance is 25



# IF using Boolean
#eEnter the type of pet
pet = input("Please enter,What type of pet would you like to insure: ")
# Apply If condition 
if (pet =="dog") or (pet =="cat"):
  print()
  print("Your insurance quote is £15pcm")
else:
  print()
  print("Your insurance quote is £25pcm")