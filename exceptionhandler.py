# Exception Handler Funcs
print('Exception Handler Funcs'.center(30, ':'))

zero = 0
one = 0

try:
    x = one/zero
    print(x)
except ZeroDivisionError:
    print('Cannot divide a number with zero')

print()