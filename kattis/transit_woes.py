time, class_time, num_buses = [int(i) for i in input().split()]
walk_times = [int(i) for i in input().split()]
ride_length = [int(i) for i in input().split()]
intervals = [int(i) for i in input().split()]

i = 0
while i < len(ride_length):
    time += walk_times[i]
    time += time % intervals[i]
    time += ride_length[i]
    i += 1

time += walk_times[-1]

if time < class_time:
    print("yes")
else:
    print("no")