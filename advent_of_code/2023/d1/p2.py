from sys import stdin

s = 0
l = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
d = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9'
}

def rev(s):
    return s[::-1]

for line in stdin.readlines():
    indexes = [x for x in list(map(line.find, l))]
    num1 = l[indexes.index(min([x for x in indexes if x != -1]))]
    if num1 in d:
        num1 = d[num1]

    indexes = [x for x in list(map(line.rfind, l))]
    print(line.strip())
    print(indexes)
    print()
    num2 = l[indexes.index(max(indexes))]
    if num2 in d:
        num2 = d[num2]

    s += int(''.join([num1, num2]))

print(s)