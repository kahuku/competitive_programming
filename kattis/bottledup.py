s, v1, v2 = map(int, input().split())
filledVolume = (s // v1) * v1
if filledVolume == s:
    print(filledVolume // v1, 0)
else:
    while filledVolume >= 0:
        if (s - filledVolume) % v2 == 0:
            print(filledVolume // v1, (s - filledVolume) // v2)
            break
        filledVolume -= v1
    else:
        print("Impossible")

# solution 2
s, v1, v2 = map(int, input().split())
filledVolume = (s // v1) * v1
while filledVolume >= 0 and (s - filledVolume) % v2 != 0:
    filledVolume -= v1
if filledVolume < 0:
    print("Impossible")
else:
    print(filledVolume // v1, (s - filledVolume) // v2)