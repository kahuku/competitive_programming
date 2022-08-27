w = int(input())
possible = w % 2 == 0 and w > 2
print("YES") if possible else print("NO")