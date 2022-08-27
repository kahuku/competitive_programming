def possible(a, b, c):
    if a + b == c:
        return True
    elif a - b == c:
        return True
    elif b - a == c:
        return True
    elif a * b == c:
        return True
    elif a / b == c:
        return True
    elif b / a == c:
        return True
    return False

for _ in range(int(input())):
    a, b, c = [int(i) for i in input().split()]
    print("Possible") if possible(a, b, c) else print("Impossible")