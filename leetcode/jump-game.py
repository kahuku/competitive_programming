class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False] * len(nums)
        reachable[0] = True
        for i in range(len(nums)):
            if reachable[i]:
                for j in range(i + 1, min(nums[i] + i + 1, len(reachable))):
                    reachable[j] = True
            if reachable[-1]:
                return True
        return reachable[-1]
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums) - 1):
            if reachable == i and nums[i] == 0:
                return False
            reachable = max(reachable, i + nums[i])
        return reachable >= len(nums) - 1