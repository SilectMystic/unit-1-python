"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def t1(a):
    return a**2 #returning the argument squared
tt1 = t1(9) #Putting the result in a variable for printing
print(tt1)
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def t2(w, l):
    return l * w #multipliyng both for area
tt2 = t2(23, 14)#Putting the result in a variable for printing
print(tt2)

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def t3(c):
    return c * 9/5 + 32 #Converting celsius to farenheit
F = t3(23)#Putting the result in a variable for printing
print(F)
"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
