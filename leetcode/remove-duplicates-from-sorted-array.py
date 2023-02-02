class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        for i in range(1, len(nums)):
            if nums[unique] != nums[i]:
                nums[unique+1] = nums[i]
                unique += 1
        return unique + 1