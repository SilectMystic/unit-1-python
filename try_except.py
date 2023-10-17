try: #Try statement for the input user error
    age = int(input('Enter your age: '))
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
except: #Telling user about wrong input
   print('Wrong value type')

try: #Try statement for division 
    faveNum = int(input('What is your favorite number: '))
    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except: #telling user about wrong input
    print('Cant divide by 0')