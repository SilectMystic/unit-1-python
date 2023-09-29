"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
a = 1
while a <= 10:
    print(a)
    a += 1
#first I made a variable with 1 and then the while loop which adds 1 and prints it
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
b = 10
while b >= 1:
    print(b)
    b -= 1
#similar to 1 i did a variable with 10 then in while loop kept taking 1 away and also printing it
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
ab = 1
i = int(input('Pick a number: '))

while i > 1:
    ab = i * ab
    i -= 1
    print(ab)
#first i put an integer and then i made the user give a number then after that i multiply it by the first variable and made the calculations then printed it
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
c = ''
while c != 'apples':
    c = input('Guess the password: ')
    if c == 'apples':
        print('congrats')
    else:
        print('try again')
#first i made a empty variable then a while loop to guess one word until they get it right
"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
p = 'Continue'
while p != 'Stop':
    asd = input('Number: ')
    dfg = input('Number 2: ')
    print(int(asd) + int(dfg))
    
    p = input('Type Continue to continue or Stop to stopo the program')
    if p == 'Stop':
        break
"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""