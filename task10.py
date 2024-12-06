# Function to get the student name
def get_student_name():
    # Ask for the student's name and return it
    student_name = input("Enter the student's name : ")
    return student_name

# Function to get the student mark
def get_student_mark():
    # Ask for the student's mark and return it
      student_mark = float(input("Enter the student's mark : "))
      return student_mark

def student_percentage(student_mark, student_name):
  if (student_mark >= 70): 
        print (student_name,"You have achieved an A Grade")
  elif (student_mark >= 60):
      print (student_name,"You have achieved a B Grade")
  elif (student_mark >= 50): 
      print (student_name,"You have achieved a C Grade")
  elif (student_mark < 50): print (student_name," You have failed")
  else:
    print("Please enter your name and marks correctly")
       
# Main code

for x in range(3):
  user = str(input("Please enter your username :"))
  pwd = str(input("Please enter your password :"))
  
  if (user != "vijaya" and pwd != "glasgow"):
    print("Incorrect credentials! You have", 2-x, "more attempts")

  else:
      print("welcome to the Grading system!")
  
      while_choice = "Y" # set the while_choice to Y so it will run at least once
      while (while_choice == "Y" or while_choice == "y"):
        student_name = get_student_name()
        student_mark = get_student_mark() 
        student_percentage(student_mark=student_mark, student_name=student_name)
        while_choice = str(input("Do you want to run the program again? (Y/N) : "))
      
      print ("You have chosen to exit the program. Goodbye!") 
      