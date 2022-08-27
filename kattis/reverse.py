num = int(input())

stack = []
for i in range(num):
    stack.append(input())

for i in range(len(stack)):
    print(stack.pop())