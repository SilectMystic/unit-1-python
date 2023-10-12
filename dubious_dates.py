import datetime #Importing needed modules from datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print(datetime.datetime.now())

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
x = (datetime.datetime.now())
print(x.strftime('%m/%d/%y %H:%M:%S'))
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
d1 = '10/11/2023'
d2 = '11/11/2023'
d3 = datetime.datetime.strptime(d1, '%m/%d/%y')
d4 = datetime.datetime.strptime(d2, '%m/%d/%y')
d5 = (d4 - d3).days()
print('The difference is ' + str(d5) + ' days')
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print('----------------------------------------')
a = int(input('year'))
b1=(x.strftime("%Y"))
d = int(b1) - a
print(d)