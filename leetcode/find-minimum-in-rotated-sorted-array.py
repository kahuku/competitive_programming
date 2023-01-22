class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = nums[0]
        for num in nums:
            if num < m:
                m = num
        return m

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

class Solution:
    findMin = min