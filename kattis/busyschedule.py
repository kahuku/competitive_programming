n = int(input())
while n != 0:
    times = [input() for _ in range(n)]

    for i in range(len(times)):
        hrs, mins, mer = times[i].replace(':', ' ').split()
        hrs, mins = int(hrs), int(mins)
        if hrs == 12: hrs = 0
        tim = mins
        tim += (60 * hrs) if mer == 'a.m.' else (60 * hrs + 12 * 60)
        times[i] = (times[i], tim)

    times = sorted(times, key=lambda x: x[1])

    for time in times:
        print(time[0])

    n = int(input())
    if n != 0: print()