class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        return [] if num % 3 else [num // 3 - 1, num // 3, num // 3 + 1]
    
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        b = int(num / 3)
        return [b - 1, b, b + 1]