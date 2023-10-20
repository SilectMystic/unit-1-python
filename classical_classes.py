"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person(): #creating class with the name person
    def __init__(self, name, age): #innit method for name and age
        self.name = name
        self.age = age
    def hi(self): #method for printing their name and age
        print('hi my name is ' + str(self.name) + ' and my age is ' + str(self.age))
t1 = Person('pablo', 98) #assigning class to a variable
t1.hi() #printing the hi method
print('------------------------------------------------------\n') #printing for separation
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animal(): #Initial class for template
    def speak(self):#method called speak to print what they say
        print()

class Dog(Animal): #Dog class using the animal template
    def speak(self):#method called speak to print what they say
        print('wuff')

class Cat(Animal):#Cat class using the animal template
    def speak(self):#method called speak to print what they say
        print('meow')

t2 = Animal() #Assigning all 3 classes to variables
t2_2 = Dog()
t2_3 = Cat()

t2.speak() #Calling all variables to print their speak method 
t2_2.speak()
t2_3.speak()
print('------------------------------------------------------\n')#printing for separation
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
class BankAccount(): #Creating class for bank account
    def __init__(self, balance, owner): #innit method for all starter needed atributes
        self.balance = balance
        self.owner = owner
    
    def total(self): #Method for printing total balance of bank
        print('Your balance is ' + str(self.balance))

    def deposit(self, depo): #method for adding deposit and printing total value
        self.balance = self.balance + depo
        print('Your total balance is ' + str(self.balance))

    def withdraw(self, withd): #method for substracting the withdraw then printing total value
        self.balance = self.balance - withd
        print('Your total balance is ' + str(self.balance))

t3_bank = BankAccount(500, 'a') #assigning class to variable
t3_bank.total() #printing total method for balance
t3_bank.deposit(200)#using deposit method for adding and printing balance
t3_bank.withdraw(100)#using withdraw method for substracting and printing balance