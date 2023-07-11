n = int(input())
drink = input()
for i in range(n, 0, -1):
    if i == 1:
        print(i, "bottle of", drink, "on the wall,", i, "bottle of", drink + ".")
        print("Take it down, pass it around, no more bottles of", drink + ".")
    elif i == 2:
        print(i, "bottles of", drink, "on the wall,", i, "bottles of", drink + ".")
        print("Take one down, pass it around,", i - 1, "bottle of", drink + " on the wall.")
        print()
    else:
        print(i, "bottles of", drink, "on the wall,", i, "bottles of", drink + ".")
        print("Take one down, pass it around,", i - 1, "bottles of", drink + " on the wall.")
        print()