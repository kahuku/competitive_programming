v = int(input())
for _ in range(int(input())):
    road, speed = input().split()
    speed = int(speed)
    if speed >= v:
        print(road, "opin")
    else:
        print(road, "lokud")