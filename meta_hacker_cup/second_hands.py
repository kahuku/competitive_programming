from collections import defaultdict
cases = int(input())
for case in range(cases):
    num_hands, k = [int(i) for i in input().split()]
    hands = [int(i) for i in input().split()]
    d = defaultdict(int)
    for hand in hands:
        d[hand] += 1
    print(f"Case #{case + 1}: NO") if (num_hands / k) > 2 or d[max(d, key=d.get)] > 2 else print(f"Case #{case + 1}: YES")
    