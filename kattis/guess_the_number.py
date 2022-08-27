high = 1000
low = 1
mid = (high + low) // 2
print(mid)
hint = input()

while hint != 'correct':
    if hint == 'lower':
        high = mid - 1
        mid = (high + low) // 2
    elif hint == 'higher':
        low = mid + 1
        mid = (high + low) // 2
    print(mid)
    hint = input()
