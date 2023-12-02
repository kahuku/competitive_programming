from sys import stdin

d = {
    'red': 12,
    'green': 13,
    'blue': 14
}

s = 0
for line in stdin.readlines():
    line = line.strip()
    game_num = int(line.split()[1][:-1])

    line = line.split(':')[1]
    games = line.split(';')

    possible = True
    for game in games:
        results = game.split(',')
        for result in results:
            n = int(result.split()[0])
            color = result.split()[1]
            if d[color] < n:
                possible = False
                break

    if possible:
        s += game_num

print(s)