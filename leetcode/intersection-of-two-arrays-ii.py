class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = 1
        output = []
        while intersection:
            s1, s2 = set(nums1), set(nums2)
            comb = s1.intersection(s2)
            for num in comb:
                if num in nums1:
                    nums1.remove(num)
                if num in nums2:
                    nums2.remove(num)
                output.append(num)
            intersection = len(comb)
            s1, s2 = set(), set()
        return output

from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            nums2, nums1 = nums1, nums2
        d = defaultdict(int)
        for num in nums1:
            d[num] += 1
        out = []
        for num in nums2:
            if d[num] > 0:
                out.append(num)
                d[num] -= 1
        return out