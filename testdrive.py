positions = [int(i) for i in input().split()]

diff1 = positions[1] - positions[0]
diff2 = positions[2] - positions[1]

if diff1 * diff2 < 0:
    print("turned")
elif abs(diff1) > abs(diff2):
    print("braked")
elif abs(diff1) < abs(diff2):
    print("accelerated")
else:
    print("cruised")
