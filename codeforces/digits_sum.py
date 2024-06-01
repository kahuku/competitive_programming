#1553A

#TLE
from functools import lru_cache

@lru_cache
def digit_sum(num):
    return int(sum([int(c) for c in str(num)]))

def is_interesting(num):
    return digit_sum(num + 1) < digit_sum(num)

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

interesting = [0] * 10
for i in range(10, max(nums) + 1):
    interesting.append(interesting[-1] + int(is_interesting(i)))

for num in nums:
    print(interesting[num])