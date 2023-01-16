# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high = n
        low = 0
        mid = high // 2
        prev = None
        while prev != mid:
            prev = mid
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
            mid = low + (high - low) // 2

        return mid