# Hash Set

class Solution:
    # O(n) time | O(n) space
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))