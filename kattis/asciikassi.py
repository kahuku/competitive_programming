n = int(input())

# first line
print('+' , end='')
for i in range(n):
    print('-', end='')
print('+')

# middle lines
for i in range(n):
    print('|', end='')
    for j in range(n):
        print(' ', end='')
    print('|')

# last line
print('+' , end='')
for i in range(n):
    print('-', end='')
print('+')