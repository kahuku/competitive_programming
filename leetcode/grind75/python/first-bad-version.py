# Binary search

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # O(log(n)) time | O(1) space
    def firstBadVersion(self, n: int) -> int:
        l = 0
        h = n
        while l < h:
            mid = (h + l) // 2
            bad = isBadVersion(mid)
            if bad:
                h = mid
            else:
                l = mid + 1
        return (h + l) // 2