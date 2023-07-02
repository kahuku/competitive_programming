mins, _ = map(int, input().split())
total_secs = mins * 60
songs = sorted(list(map(int, input().split())))
secs = 0
i = 0
while i < len(songs) and secs + songs[i] <= total_secs:
    secs += songs[i]
    i += 1
print(secs)