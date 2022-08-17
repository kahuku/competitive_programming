statements = int(input())
x = 0
for statement in range(statements):
    operation = input()
    if '++' in operation:
        x += 1
    elif '--' in operation:
        x -= 1
print(x)