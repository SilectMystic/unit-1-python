"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
a = 'hola'
for letters in a:#Iterate each character separated
    print(letters)
print('------------------------------------------------------')#This is just separation
"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
b = [1, 2, 3]
l = 0 #To store the sum
for num in b:
    l += num #To add all numbers inside original variable with for loop
print(l)#Print entire sum
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print('------------------------------------------------------')
o = 'hola soy dora'
p = (o.split(' ')) #Splitted the sentece into a list
for let in p: #Loop to get each character
    print(let)#Print items
    print(len(let))#Print character lenght
print('------------------------------------------------------')
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
#It is what i expected since its a dictionary i expected to do extra code in order to get both key and values so a simple print statement would only do the keys
pa = {
    'ha': 'pa',
    'ja':'ba',
    'lo':'co',
    'ho':'la'
}

for x in pa: #Iteration for each item on dictionary
    print(x)