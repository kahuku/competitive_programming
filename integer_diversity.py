cases = int(input())
for _ in range(cases):
    n = int(input())
    nums = [int(i) for i in input().split()]
    s = set()
    for num in nums:
        if num not in s:
            s.add(num)
        else:
            s.add(-1 * num)
    print(len(s))