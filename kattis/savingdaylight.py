from sys import stdin
for line in stdin.readlines():
    month, day, year, sunrise, sunset = line.split()
    rise_hour, rise_minute = map(int, sunrise.split(':'))
    set_hour, set_minute = map(int, sunset.split(':'))
    rise = rise_hour * 60 + rise_minute
    set = set_hour * 60 + set_minute
    diff = set - rise
    hour = diff // 60
    minute = diff % 60
    print(month, day, year, hour, 'hours', minute, 'minutes')