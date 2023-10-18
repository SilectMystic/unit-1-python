"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def t1(a):#function with parameter for squared result
    return a**2 #returning the argument squared
try: #Try and except statement for assert test
    assert t1(7) == 49
    assert t1 (4) == 16
except:
    print('Incorrect value output on Task 1') #Print if assert is false
print(t1(9)) #Printing result with given parameter
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def t2(w, l):#function with parameter needed for formula 
    return l * w #multipliyng both for area
try:#Try and except statement for assert test
    assert t2(41, 24) == 984
    assert t2(98, 16) == 1568
except:
    print('Incorrect value output on Task 2')#Print if assert is false
print(t2(23, 14))#Printing result with given parameter

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def t3(c): #function with parameter for temperature
    return c * 9/5 + 32 #Converting celsius to farenheit
try:#Try and except statement for assert test
    assert t3(13) == 55.4
    assert t3(75) == 167
except:
    print('Incorrect value output on Task 3')#Print if assert is false
print(t3(23))#Printing result with given parameter
"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def t4(x): #Function with parameter for list
    total = sum(x) #Putting the sum of list on total
    return total / len(x) #returning the average of list

try:#Try and except statement for assert test
    assert t4([1,2,3,4]) == 2.5
    assert t4([5,6,7,8,9]) == 7
except:
    print('Incorrect value output on Task 4')#Print if assert is false

print(t4([1,5,6,4,7,9]))