todos = ['Add a todo!']
a = True
while a == True:
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nHere is your list\n')
    k = 1
    for items in todos:
        print(str(k) + '. ' + items)
        k += 1
    print()
    b = input('Would you like to add more or remove? (add, rem): ')
    if b == 'add':
        todos.append(input('\nAdd your item: '))
        print('\nYour item was added!')
        todos.remove('Add a todo!')
    elif b == 'rem':
        try:
            c = int(input('\nWhat number you want to delete? '))
            c -= 1
            todos.pop(c)
            print('\nYour item was removed!')
        except ValueError:
            print('\n(Please give an available number)')
    else:
        print('\n(Please give correct input)')