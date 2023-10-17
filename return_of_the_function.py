"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def t1(a):#function with parameter for squared result
    return a**2 #returning the argument squared
print(t1(9)) #Printing result with given parameter
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def t2(w, l):#function with parameter needed for formula 
    return l * w #multipliyng both for area
print(t2(23, 14))#Printing result with given parameter

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def t3(c): #function with parameter for temperature
    return c * 9/5 + 32 #Converting celsius to farenheit
print(t3(23))#Printing result with given parameter
"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def t4(m,l,j,h,e,a):#Making function with parameters for sum of average
    return m+l+j+h+e+a #sum for average 
print(t4(1,5,6,4,7,9)/6)#Printing result with given parameter