# Array, Hash Table

from collections import Counter

class Solution:
    # O(n) time | O(n) space
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common(1)[0][0]
    
class Solution:
    # O(n) time | O(1) space
    def majorityElement(self, nums: List[int]) -> int:
        ma = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                ma = nums[i]
                count = 1
            elif nums[i] == ma:
                count += 1
            else:
                count -= 1
        return ma

class Solution:
    # O(nlog(n)) time | O(1) space
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]