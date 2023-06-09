from sys import stdin
for line in stdin.readlines():
    nums = list(map(int, line.split()))
    s = sum(nums)
    nums = set(nums)
    for n in nums:
        if s - n == n:
            print(s - n)
            break