from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
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
