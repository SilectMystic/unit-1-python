# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
def greet(name): #name paratemer for printing users name
    print('Hi ' + name) #Printing both hi string and name parameter
greet('Torres')

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.
def sum_numbers(a, b): 
    print(a + b) #Adding both numbers together to print
sum_numbers(5, 9)

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.
def factorial(n): #N parameter for the factorial number
    ab = 1 #Initial variable with 1
    while n > 1: #To make it loop until its down to 1
        ab = n * ab #Multiplying it by the variable 
        n -= 1 #Subtracting one from the parameter
    print(ab)
factorial(9)

# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.
def is_even(num): #Num parameter for testing if number is even
    if num % 2 == 0: #Checking remaindor for either even or non even
        print('True')
    else: #For non even
        print('False')
is_even(5)
# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.
def calculate_area(length, width): #length or width to calculate area
    n = length * width #multiplying both parameters
    print(n)
calculate_area(32, 20)