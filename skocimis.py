inp = [int(i) for i in input().split()]

a, b, c = inp[0], inp[1], inp[2]
l = [a, b, c]

#print(l)

count = 0
while l[2] - l[1] != 1 or l[1] - l[0] != 1:
    diff1 = l[2] - l[1]
    diff2 = l[1] - l[0]
    if diff1 < diff2:
        #place 3 1 above 1
        l[2] = l[0] + 1
        l.sort()
    else:
        #place 1 1 above 2
        l[0] = l[1] + 1
        l.sort()
    count += 1
print(count)
