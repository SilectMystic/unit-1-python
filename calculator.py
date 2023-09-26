print('Welcome to the calculator')
print()
# hi, welcome to the calculator
try:
    a = float(input('Input the first number: '))
    print()
    b = float(input('Input the second number: '))
    print()
    print('''Select operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Floor Division
    6. Exponential
    7. Remainder''')
    c = int(input())
    print()
    #here i do multiple input in order to get the 3 inputs from the user.

    if c == 1:
        d = a + b
        print(d)
    elif c == 2:
        d = a - b
        print(d)
    elif c == 3:
        d = a * b
        print(d)
    elif c == 4:
        if a or b == 0:
            print('Please put a number higher than 0')
        else:
            d = a / b
            print(d)
        #here i did an extra if statement in order to catch a 0 with the division and to tell the user to not do that
    elif c == 5:
        d = a // b
        print(d)
    elif c == 6:
        d = a ** b
        print(d)
    elif c == 7:
        d = a % b
        print(d)
    else:
        print('Please put a number on the list of operators')
#in this if statement it does all the calculations with the if and elif running depending on the c variable for the calculations
#and then ending with an else in order to catch any higher numbers than the 1 to 7 for the c variable
except ValueError:
    print('Please use numbers!')
#the try and except statements what they do here is that the try statement will run first and if there is any error inside the try code
#then the except code will run with the print statement