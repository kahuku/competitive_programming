a, b = list(map(int, input().split()))
while a != 0 or b != 0:
    if a + b == 13:
        print("Never speak again.")
    elif a == b:
        print("Undecided.")
    elif a > b:
        print("To the convention.")
    else:
        print("Left beehind.")
    a, b = list(map(int, input().split()))