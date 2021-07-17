# If Conditional Funcs
print('If Conditional Funcs'.center(30, ':'))

number = 5

if number > 6:
    print('Angka {} lebih besar dari 6'.format(number))
elif number < 6:
    print('Angka {} lebih kecil dari 6'.format(number))
else:
    print('Angka {} sama dengan 6'.format(number))

print()


# Ternary Operator Funcs
print('Ternary Operator Funcs'.center(30, ':'))

yes = True
no = False

print('Accepted' if yes else 'Rejected')
print('Accepted' if no else 'Rejected')

print(('Rejected', 'Accepted')[yes])
print(('Rejected', 'Accepted')[no])

print()


# String Loop Funcs
print('String Loop Funcs'.center(30, ':'))

name = []

for word in 'kuntiarso':
    name.append(word)

print(name)

print()


# List/Index Loop Funcs
print('List/Index Loop Funcs'.center(30, ':'))

arr = ['kuntiarso', '20', 'indonesia']

for data in arr:
    print('data: {}'.format(data))

print()

for data in range(len(arr)):
    print('data: {}'.format(arr[data]))

print()


# For Else Funcs
print('For Else Funcs'.center(30, ':'))

for number in range(10, 21):
    if (number < 10):
        print('number: {}'.format(number))
        break
else:
    print('no one numbers have found')

print()


# Pass Funcs
print('Pass Funcs'.center(30, ':'))

def first_function():
    pass

import sys

name = ''

# while(name != 'kuntiarso'):
while(False):
    try:
        name = input('Please enter my name to be accepted: ')
        print('your input is: {}'.format(int(name)))
    except:
        if name == 'kuntiarso':
            pass
        else:
            print('error: your input \'{}\' is wrong'.format(name))

print()


# List Comprehension Funcs
print('List Comprehension Funcs'.center(30, ':'))

numbers = [1, 4, 5, 8]
quadrates = [n**2 for n in numbers]
print(quadrates)

arr1 = ['a', 'f', 'g', 'r', 'p', 'm']
arr2 = ['g', 'q', 'w', 'm', 'p', 'z']
duplicates1 = [one for one in arr1 for two in arr2 if one == two]
duplicates2 = [two for one in arr1 for two in arr2 if one == two]
print(duplicates1)
print(duplicates2)

titles = ['Kuntiarso', 'Riyadi', 'Riza', 'Hello', 'World']
lowers = [title.lower() for title in titles]
uppers = [title.upper() for title in titles]
print(lowers)
print(uppers)

nested_arr = [[n**2, n**3] for n in range(1, 10, 2)]
print(nested_arr)

print()
