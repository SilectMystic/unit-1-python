"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
a = ["a","b",'c','d']
print(a)
#First i made a list called a and then put a to d in order then printed it
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
a.append('e')
print(a)
#First i used append and added e to the list then printed it
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
a.remove('e')
print(a)
#I used the remove statement in order to remove the e that i added with append then printed
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
a[0] = 'A'
print(a)
#First i updated the value at position 0 and then printed it
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
a.append('e')
a.append('f')
print(a)
#Fist i appended two new letters and then printed it.
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del a[5]
print(a)
#I used the del element to delete f which is in the 5 position and then printed it
"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
lkj = a[:2]
print(lkj)
#First i made a new variable called lkj and then i made it call the list with 2 ranged values and then printed the variable which has 2 list items
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
asdf = ['asf','ert']
b = a + asdf
print(b)

#First i made a brand new list and then combined them by making a new variable and then combining both lists in there then printing it