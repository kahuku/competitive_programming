cases = int(input())
for case in range(cases):
    r, e, c = [int(i) for i in input().split()]
    delta = e - (r + c)
    if delta > 0:
        print("advertise")
    elif delta < 0:
        print("do not advertise")
    else:
        print("does not matter")