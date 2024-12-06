function authenticate_user():
          
    set correct_username = "vijaya"
    set correct_password = "glasgow"
    
    
    while attempts > 0:
        If username == correct_username and password == correct_password:
            print "Login successful!"
            Return True
        Else:
            decerment attempt by 1
            print "Incorrect login. You have X attempt(s) left."
            if attempts grater than 0:
                print user for username and password again.
			Else
				print "Too many failed login attempts."
			return False


Function display_menu():
   Initialize wages as empty list
    
    while True:
        print"\n--- Menu ---"
        print"1. Read data from file"
        print"2. Calculate Wages (add to list)"
        print"3. Print Wages"
        print"4. Find Max Wage"
        print"5. Find Min Wage"
        print"6. Count Wages under £100"
        print"7. Exit"
        
       Prompt user for choice (1 to 7)
        
        if choice == 1
             set wages = read_data_from_file("wages.txt")
			 
        elif choice == 2
	         print"Wages already added from the file."
			 
        elif choice == 3
            call print_wages(wages)
			
        elif choice == 4
            max_wage = find_max_wage(wages)
            print"Max wage: £" + max_wage
			
        elif choice == 5
            min_wage = find_min_wage(wages)
            print"Min wage: £" + min_wage
			
        elif choice == 6
            count_under_100 = count_wages_under_100(wages)
            print f"Number of wages under £100: {count_under_100}"
			
        elif choice == 7
            print "Exiting the program."
            break
        else:
            print "Invalid choice. Please try again."


Function read_data_from_file(file_name):
    Initialize wages as empty list
    Open file "wages.txt" in read mode
    
    For each line in file:
        Split line into name and wage
        Convert wage to float
        Append wage to wages list
        
    Close the file
    Return wages list

Function print_wages(wages):
    If wages is empty:
        Print "No wages to display."
    Else:
        For each wage in wages:
            Print "Wage: £" + wage

Function find_max_wage(wages):
    If wages is empty:
        Return "No wages to calculate max."
    Else:
        Return max(wages)

Function find_min_wage(wages):
    If wages is empty:
        Return "No wages to calculate min."
    Else:
        Return min(wages)

Function count_wages_under_100(wages):
    Initialize count as 0
    For each wage in wages:
        If wage < 100:
            Increment count by 1
    Return count

Main function:
    If authenticate_user() is True:
        Call display_menu()
    Else:
        Print "Exiting the program due to failed login attempts."

End


