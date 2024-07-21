nFriends, nDays, today = map(int, input().split())
goodDate = today + nDays - 14
friends = 0
for _ in range(nFriends):
    day = int(input())
    if day <= goodDate:
        friends += 1
print(friends)