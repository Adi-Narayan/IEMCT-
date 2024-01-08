print("Which operation do you need to perform \n")
print(" Addition (+)\n Subtraction (-)\n Multiplication (*)\n Division (/)\n Modulus (%)\n Exponent (**)\n")
ch = input()

if ch == '+':
    print("Enter the numebrs to be added")
    a = int(input())
    b = int(input())
    print(a + b)
elif ch == '-':
    print("Enter the numebrs to be subtracted")
    a = int(input())
    b = int(input())
    print(a - b)
elif ch == '*':
    print("Enter the numebrs to be multiplied")
    a = int(input())
    b = int(input())
    print(a * b)
elif ch == '/':
    print("Enter the numebrs to be divided")
    a = int(input())
    b = int(input())
    print(a / b)
elif ch == '%':
    print("Enter the numebrs for which the modulus operation is to be performed")
    a = int(input())
    b = int(input())
    print(a % b)
elif ch == '**':
    print("Enter the root and the power")
    a = int(input())
    b = int(input())
    print(a**b)
else:
    print("Invalid Input")
 