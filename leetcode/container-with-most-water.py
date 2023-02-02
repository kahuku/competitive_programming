class Solution:
    def maxArea(self, height: List[int]) -> int:
        def vol(a, b): return min(height[a], height[b]) * (b - a)
        left, right = 0, len(height) - 1
        biggest = 0
        while left < right:
            if vol(left, right) > biggest:
                biggest = vol(left, right)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return biggest