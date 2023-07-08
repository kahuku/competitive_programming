orders, tank_size = map(int, input().split())
tank = tank_size
count = 0
for _ in range(orders):
    i = input()
    n = int(i[0])
    if len(i) > 1 and i[1] == 'L': n += 1
    if tank - n < 0:
        count += 1
        tank = tank_size - n
    else:
        tank -= n
print(count)