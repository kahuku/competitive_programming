import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.current = nums.copy()

    def reset(self) -> List[int]:
        self.current = self.original.copy()
        return self.current

    def shuffle(self) -> List[int]:
        random.shuffle(self.current)
        return self.current


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()