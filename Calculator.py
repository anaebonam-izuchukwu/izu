#A simple calculator 
import math
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Sine")
print("6. Cosine")
print("7. Tan")
while True:
    Operation = input("Enter Operation (1/2/3/4/5/6/7): ")

    if Operation in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
       
        if Operation == '1':
            print("Result:", (num1+num2))
        elif Operation == '2':
            print("Result:", (num1-num2))
        elif Operation == '3':
            print("Result:", (num1*num2))
        elif Operation == '4':  
            print("Result:", (num1/num2))
        break
    else: Operation in ['5','6','7']
    num3 = float(input("Enter an angle:  "))
    num3 = math.radians(num3)
    if Operation == '5':
            print("Result:", math.sin(num3))
    elif Operation == '6':
            print("Result:", math.cos(num3))
    elif Operation == '7':
            print("Result:", math.tan(num3))    
    break

