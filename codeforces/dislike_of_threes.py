polycarp = [num for num in range(1, 1667) if num % 3 != 0 and str(num)[-1] != '3']
[print(polycarp[int(input()) - 1]) for _ in range(int(input()))]