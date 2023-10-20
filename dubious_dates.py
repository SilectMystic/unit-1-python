import datetime #Importing needed modules from datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print(datetime.datetime.now()) #Printing date and time using the datetime now module
print('----------------------------------------\n')#separation

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
x = (datetime.datetime.now()) #assigning datetime now in a variable for later use
print(x.strftime('%m/%d/%y %H:%M:%S')) #using x variable with strftime filter for proper format
print('----------------------------------------\n') #separation
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
d1 = '10/11/2023' #Variables to convert
d2 = '11/11/2023'
d3 = datetime.datetime.strptime(d1, '%m/%d/%Y') #Converting both variable into usable integers
d4 = datetime.datetime.strptime(d2, '%m/%d/%Y')
d5 = d4 - d3 #Substracting the difference
print('The difference is ' + str(d5) + ' days.') #Printing the difference between two given dates
print('----------------------------------------\n')#separation
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
a = int(input('Year: ')) #Input for their birthdate
print()
b1=(x.strftime("%Y")) #strftime calling for current year using the same x variable from before
d = int(b1) - a #substracting both given year and x variable year
print('You are ' + str(d)) #Printing the difference