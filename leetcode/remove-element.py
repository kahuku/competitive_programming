class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        last_index = len(nums) - 1
        for i, num in reversed(list(enumerate(nums))):
            if num == val:
                nums[i], nums[last_index] = nums[last_index], '_'
                last_index -= 1
            else:
                count += 1
        return count