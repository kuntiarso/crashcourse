# Justify Text Funcs
print('Justify Text Funcs'.center(30, ':'))

right1 = 'kuntiarso'.rjust(20)
right2 = 'kuntiarso'.rjust(20, '-')
print(right1)
print(right2)

left1 = 'kuntiarso'.ljust(20)
left2 = 'kuntiarso'.ljust(20, '-')
print(left1)
print(left2)

center1 = 'kuntiarso'.center(20)
center2 = 'kuntiarso'.center(20, '-')
print(center1)
print(center2)

print();


# Range Loop Funcs
print('Range Loop Funcs'.center(30, ':'))

arr1 = []
for i in range(5):
    arr1.append(i)

print(arr1)

arr2 = []
for i in range(1, 11):
    arr2.append(i)

print(arr2)

arr3 = []
for i in range(1, 11, 2):
    arr3.append(i)

print(arr3)

print()


# In and Not In Funcs
print('In and Not In Funcs'.center(30, ':'))

sentence = 'Learn how to code python programming language'
print('learn' not in sentence)
print('learn' in sentence)
print('python' not in sentence)
print('python' in sentence)

print()


# Unpack Values Funcs
print('Unpack Values Funcs'.center(30, ':'))

arr = ['kuntiarso', '20', 'indonesia']
name, age, country = arr
print(name + ', ' + age + ', ' + country)

tup = ('kuntiarso', '20', 'indonesia')
name, age, country = tup
print(name + ', ' + age + ', ' + country)

print()