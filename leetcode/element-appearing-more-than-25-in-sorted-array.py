# O(n)
from collections import defaultdict
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for num in arr:
            d[num] += 1
        return sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0]
    
# O(n) O(1) space
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l = len(arr) // 4
        for i in range(0, len(arr) - l):
            if arr[i] == arr[i + l]:
                return arr[i]
        return -1