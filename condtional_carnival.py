'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''
bas = int(input('Enter a number: '))
bas = bas % 2
if bas == 0:
    print('Its and even number.')
else:
    print('Its an odd number')
#first i asked for input and then got the remainder to see if its even or not
'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

EXTRA CREDIT: Tell the user if they did not enter a valid number
'''
try:
    ap = float(input('Enter a number: '))
except ValueError:
    print('wrong value type')
if ap <= -1:
    print('Its a negative number.')
elif ap == 0:
    print('Its a zero')
else:
    print('Its positive')
# first i asked for input and then i checked using if else for negative and positive
'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''
a = [1,2,3]
b = max(a)
print(b)
#first i made a list and then got the max using the max statement and then printed it in a variable 
'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
by = int(input('Enter year: '))
if by % 4 ==0:
    print('This is a leap year')
else:
    print('Not a leap year')
#first i got the year by using the input and then i used % to get the remainder by 4 and then get if its a leap year
'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''
try:
    ips = str(input('Enter a character: '))
except ValueError:
    print('Input needs to be text')

vowel = ['a','e','i','o','u']

for letter in vowel:
    if letter in ips:
        print('Its a Vowel')
        break
    else:
        print('Its a consonant')
    break
#First i asked for str input and then i made a list with vowels and then made a loop to check multiple characters in a input to check if they are either vowels or the other one