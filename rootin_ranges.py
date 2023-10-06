"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
#For loop with range of 11 for output max 10
for x in range(11):
    print(x)#Printing each number by iteration
print('------------------------------------------------------')
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for c in range(900, 1001, 10): #For loop with range with requested numbers
    print(c)#Printing each number in range by iteration
print('------------------------------------------------------')
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
for v in range(1, 101, 9):#For loop with range with requested numbers
    print(v)#Printing each number in range by iteration
print('------------------------------------------------------')
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
sum = 0#Empty variabel for total sum
for b in range(1, 11):#For loop with range with requested numbers
    sum += b #Adding number per iteration in sum using range
    print(sum)#Printing value of sum by each iteration using range
print('------------------------------------------------------')
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5
 
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()

#The output is * sign in 5 rows and every row has one more
#Through every iteration it adds one number to i variable made in first loop which is shared between both for loops
#then prints more stars by the i variable