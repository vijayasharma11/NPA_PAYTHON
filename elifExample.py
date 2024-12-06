 # get student name
studentName = input("Enter Student Name:")
# get student mark
studentMark = int(input("Enter Student Mark:"))

# if mark is 70 or over
if studentMark >= 70 : 
  print(studentName + ": A Grade")

  # if mark is 60 or over
elif studentMark >= 60 : 
    print(studentName +": B Grade")

  # if mark is 50 or over
elif studentMark >=50 : 
  print(studentName +": C Grade")
  

  # if no match we use this option
else: 
  print(studentName +":failed")