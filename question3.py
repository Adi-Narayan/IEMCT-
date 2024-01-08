print("Which operation do you need to perform \n")
print(" Addition (+)\n Subtraction (-)\n Multiplication (*)\n Division (/)\n Modulus (%)\n Exponent (**)\n")
ch = input()

def add():
    print("Enter the numebrs to be added")
    a = int(input())
    b = int(input())
    print(a + b)

def sub():
    print("Enter the numebers to be subtracted")
    a = int(input())
    b = int(input())
    print(a - b)

def mul():
    print("Enter the numebers to be multiplied")
    a = int(input())
    b = int(input())
    print(a * b)

def div():
    print("Enter the numebers to be divided")
    a = int(input())
    b = int(input())
    print(a / b)

def mod():
    print("Enter numebers for which the modulus operation is to be performed")
    a = int(input())
    b = int(input())
    print(a % b)

def exp():
    print("Enter the root and the power")
    a = int(input())
    b = int(input())
    print(a**b)

if ch == '+':
    add()
elif ch == '-':
    sub()
elif ch == '*':
    mul()
elif ch == '/':
    div()
elif ch == '%':
    mod()
elif ch == '**':
   exp()
else:
    print("Invalid Input")
 
