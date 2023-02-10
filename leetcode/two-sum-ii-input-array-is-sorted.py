class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        tot = numbers[l] + numbers[r]
        while tot != target:
            if tot > target:
                r -= 1
            else:
                l += 1
            tot = numbers[l] + numbers[r]
        return [l + 1, r + 1]