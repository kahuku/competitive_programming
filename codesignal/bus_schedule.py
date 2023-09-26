# Visa 2024 summer intern application

# given a list of times for bus arrivals and the current time, determine how long the user has to wait for the next bus

def solve(times, current_time):
    mins_times = []
    for time in times:
        mins_times.append(int(time[:2]) * 60 + int(time[3:]))
    current_time = int(current_time[:2]) * 60 + int(current_time[3:])
    for time in mins_times:
        if time > current_time:
            h = str(time // 60)
            m = str(time % 60)
            if len(h) == 1:
                h = "0" + h
            if len(m) == 1:
                m = "0" + m
            return h + ":" + m
    return "-1"