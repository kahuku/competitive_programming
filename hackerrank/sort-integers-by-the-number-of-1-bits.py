# JPMorgan summer SWE 2024 intern app
# sort list of integers by the number of 1 bits in their binary representation and then by their base10 value
from collections import defaultdict

def sortByBits(arr):
    bins = [bin(num).count('1') for num in arr]
    count = defaultdict(int)
    for num in arr: count[num] += 1
    d = {arr[i]: (bins[i], arr[i], count[arr[i]]) for i in range(len(arr))}
    l = sorted(d.items(), key=lambda x: (x[1][0], x[1][1]))
    out = []
    for item in l:
        c = item[1][2]
        while c > 0:
            c -= 1
            out.append(item[0])
    return out

if __name__ == "__main__":
    sortByBits([0,1,2,3,4,5,6,7,8])
