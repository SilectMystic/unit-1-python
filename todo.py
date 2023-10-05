todos = ['Add a todo!'] #The list for the todo with an item called Add a todo for the user to know.
while 1: #Start of the infinite while loop
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') #Separation for iteration run 
    print('\nHere is your list\n') #Guiding user to where is the list
    k = 1 #Index
    for items in todos: #Loop for items and index
        print(str(k) + '. ' + items) #Print both k index variable and item
        k += 1 #To increase the index number
    print()
    b = input('Would you like to add more or remove? (add, rem): ') #To collect what user wants to do
    if b == 'add':
        todos.append(input('\nAdd your item: ')) #Adds the item from user input
        print('\nYour item was added!')
        if 'Add a todo!' in todos:
            todos.remove('Add a todo!') #To remove item placeholder only when its there
    elif b == 'rem':
        try: #To avoid code error on incorrect input value
            c = int(input('\nWhat number you want to delete? '))
            c -= 1 #To keep withing normal counting from 1 not 0
            todos.pop(c) #To remove item using input -1
            print('\nYour item was removed!')
        except IndexError: #To avoid input error of higher index number
            print('\n(Please give an available number)')
        except ValueError: #To avoid input error of non-integer
            print('\n(Please give an available number)')
    else: #To tell user to use available commands
        print('\n(Please give a correct input)')