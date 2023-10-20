"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hi(self):
        print('hi my name is ' + str(self.name) + ' and my age is ' + str(self.age))
t1 = Person('pablo', 98)
t1.hi()
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animal():
    def speak(self):
        print()

class Dog(Animal):
    def speak(self):
        print('wuff')
class Cat(Animal):
    def speak(self):
        print('meow')

t2 = Animal()
t2_2 = Dog()
t2_3 = Cat()

t2.speak()
t2_2.speak()
t2_3.speak()
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
class BankAccount():
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
    