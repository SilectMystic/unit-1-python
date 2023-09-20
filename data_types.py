"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
a = 1.0
print(a)
print(int(a))
#First I made a variable with 1.0 and then just made two print statements one just printing a and the other converting a into integer.
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
c = int(input("Numero porfavor: "))
if c >= 1:
    print("Positive")
elif c == 0:
    print("Zero")
else:
    print("Negative")
#First i asked for a number as a integer and then i made a if statement checking for more or equal to 1 for positive then elif to search equals
#to 0 for zero and then elif for negative
"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
f = int(input("Give me a integer: "))
e = float(input("Give me a float: "))
add = f + e
sub = f - e
mult = f * e
div = f / e
print(add, sub, mult, div)
#First i asked for two inputs one for integer and then one for float after that i made different variables duing the math it accords
#for example add is f + e and then i printed it all together because of limited time
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
fruits = {
    "apple": 12,
    "oranges": 13
}
print(fruits["oranges"])
#I made a dictionary called fruits and then i just printed the value for oranges inside the dictionary
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
happa = "1,2,3,4,5,6,7,8"
happa_tup = happa.split(",")
print(tuple(happa_tup))
#First i made a variable with 1 to 8 with no spaces and with "," and then i made another variable in order to split the numbers from
#the commas and then i converted it to a tuple in the print statement