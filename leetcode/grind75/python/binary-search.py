# Search, binary search

class Solution:
    # O(logn) time | O(1) space
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        mid = (hi + lo) // 2
        while lo <= hi:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
            mid = (hi + lo) // 2
        return -1