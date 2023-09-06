a1, b1, a2, b2 = map(int, input().split())
c1, d1, c2, d2 = map(int, input().split())
gunnar = (a1 + b1 + a2 + b2) / 2
emma = (c1 + d1 + c2 + d2) / 2
if gunnar == emma:
    print("Tie")
else:
    print("Gunnar" if gunnar > emma else "Emma")