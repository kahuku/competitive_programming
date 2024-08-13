# Round 966

for _ in range(int(input())):
    num = input()

    if len(num) < 3:
        print("NO")
        continue

    if num[0] != '1' or num[1] != '0':
        print("NO")
        continue

    if num[2] == '1' and len(num) == 3:
        print("NO")
        continue

    if num[2] == '0':
        print("NO")
        continue

    print("YES")
    