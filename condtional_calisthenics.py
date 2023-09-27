'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
a = 10
if a >= 10:
    print('True')
else:
    print('False')
#First i made a variable and then i made a >= to ten in order to give an true or false result
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
b = int(input('Ponga su edad: '))
c = input(' Educacion????')
if b < 18 or c == 'yes':
    print('Price would be $10')
else:
    print('Price would be $20')
#First i asked the user for their age and then their education and after i used an if statement with an or in order to check for both 
#then i made an else to make sure if both are false they would pay 20
'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruits = ['apples', 'oranges', 'watermelon']
g = input('Give me a fruit name: ')
if g in fruits:
    print('Yes, that fruit is in the list.')
else:
    print("No, that fruit is not in the list.")
#first i made a list with 3 fruits then after i made an input and a if statement checking if they got it right
'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
y = int(input('Enter year: '))
if y % 4 == 0:
    print('The year is a leap year')
elif y % 100 == 0:
    print('The year is a century year')
else:
    print('The year is neither century or leap')
#First i asked for a year input and the used if elif and else to check for both leap and century year and then for the rest if both
#are flase they would have neither century or leap print
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
w = input('Please input package weigth: ')
z = input('Please input zone (A or B): ')
if z == 'A':
    p = float(w) * 5
    print('The price for zone A would be ' + p)
elif z == 'B':
    p = float(w) * 7
    print('The price for zone B would be ' + p)
else:
    print('Please put a valid zone')
#first i asked for two inputs for zone and weight and then i did an if statement comparing the zone input first and then multiplying
#the weight for the price per kilogram.
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
