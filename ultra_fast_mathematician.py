def xor(a, b):
    return '1' if bool(a) ^ bool(b) else '0'

num1 = input()
num2 = input()
s = ''
for i in range(len(num1)):
    s += xor(int(num1[i]), int(num2[i]))
print(s)