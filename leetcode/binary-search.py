class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        mid = (high + low) // 2
        while high >= low:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            mid = (high + low) // 2
        return -1
            
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high, mid = 0, len(nums) - 1, 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1