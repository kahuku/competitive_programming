class Solution:
    def pivotInteger(self, n: int) -> int:
        n = list(range(n + 1))
        pre = list(accumulate(n, operator.add))
        for i in range(1, len(pre)):
            left = pre[i] - pre[0]
            right = pre[-1] - pre[i-1]
            if left == right:
                return i
        return -1

class Solution:
    def pivotInteger(self, n: int) -> int:
        n = list(range(n + 1))
        pre = list(accumulate(n, operator.add))
        post = list(accumulate(n[::-1], operator.add))[::-1]
        for i in range(len(n)):
            if pre[i] == post[i]:
                return i
        return -1

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        low, high = 1, n
        n = list(range(1, n+1))
        while low < high:
            mid = (high + low) // 2
            left, right = sum(n[:mid+1]), sum(n[mid:])
            print(mid, left, right)
            if left == right:
                return mid + 1
            elif left < right:
                low = mid + 1
            else:
                high = mid
        return -1