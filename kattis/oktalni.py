d = {
    '000': '0',
    '001': '1',
    '010': '2',
    '011': '3',
    '100': '4',
    '101': '5',
    '110': '6',
    '111': '7'
}

b = input()
if len(b) % 3 == 1:
    b = '00' + b
elif len(b) % 3 == 2:
    b = '0' + b
o = ''
for i in range(0, len(b), 3):
    o += d[b[i:i+3]]
print(o)