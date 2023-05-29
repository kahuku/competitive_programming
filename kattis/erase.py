x = int(input())
a, b = input(), input()
if x % 2 == 0:
    print("Deletion succeeded" if a == b else "Deletion failed")
else:
    c = sum(1 for la, lb in zip(a, b) if la != lb)
    print("Deletion succeeded" if c == len(a) else "Deletion failed")