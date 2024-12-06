firstNumber = float(input("Enter first float Number: "))
secondNumber = float(input("Enter Second float Number: "))
operation = input("Enter opration to perform (+ or -): ")
print(type(operation))
answer = None
if(operation == "+"):
    answer = firstNumber + secondNumber
elif (operation == "-"):
    answer = firstNumber - secondNumber
else:
    print("Unsupported operation")
print(answer)

