from collections import Counter
print("yes") if max(Counter(input().split()).values()) <= 1 else print("no")