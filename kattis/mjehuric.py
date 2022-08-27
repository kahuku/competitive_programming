#mjehuric

def print_order(l):
    print(l[0], " ", l[1], " ", l[2], " ", l[3], " ", l[4])

def swap(l, i1, i2):
    tmp = l[i2]
    l[i2] = l[i1]
    l[i1] = tmp
    print_order(l)
    return l

order = [int(i) for i in input().split()]
sortd = order.copy()
sortd.sort()

#print(order)
#print(sortd)

while sortd != order:
    #print(order)
    if order[0] > order[1]:
        order = swap(order, 0, 1)
    if order[1] > order[2]:
        order = swap(order, 1, 2)
    if order[2] > order[3]:
        order = swap(order, 2, 3)
    if order[3] > order[4]:
        order = swap(order, 3, 4)
        
    

