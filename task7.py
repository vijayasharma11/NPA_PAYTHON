
attempts  = 0;
#set a correct username and password
correct_username = "vijaya"
correct_password = "glasgow"

for attempts in range(4):
 username = input("Enter your username :")
 password = input("Enter your password : ")

 if (username == correct_username and password == correct_password) :
    print("Login sucessful!")
    break
 else :
   attempts += 1
   print("Incorrect username or password.Please try agian")

if(attempts == 4) :
  print("To many failed attempts.Access denied")

 
