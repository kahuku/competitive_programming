class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [float('inf')] * len(nums)
        jumps[0] = 0
        for i in range(len(nums)):
            if jumps[i] != float('inf'):
                for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
                    jumps[j] = min(jumps[j], jumps[i] + 1)
        return jumps[-1]
    
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, end, furthest = 0, 0, 0
        for i in range(len(nums) - 1):
            furthest = max(furthest, nums[i] + i)
            if furthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:
                end = furthest
                ans += 1
        return ans