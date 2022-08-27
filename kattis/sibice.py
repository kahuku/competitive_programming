inp = input()
l = inp.split(' ')
n = int(l[0])
x = int(l[1])
y = int(l[2])

matches = []
for i in range(n):
    matches.append(int(input()))

for entry in matches:
    if entry <= ((x**2 + y**2)** 0.5):
        print("DA")
    else:
        print("NE")
