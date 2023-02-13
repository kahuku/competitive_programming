class NumArray:

    def __init__(self, nums: List[int]):
        self.running = [0, nums[0]]
        for i in range(1, len(nums)):
            self.running.append(nums[i] + self.running[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.running[right + 1] - self.running[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class NumArray:

    def __init__(self, nums: List[int]):
        self.running = [nums[0]]
        for i in range(1, len(nums)):
            self.running.append(nums[i] + self.running[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.running[right] - self.running[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)