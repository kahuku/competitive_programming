#1907A
import string

boardw = range(1, 9)
boardh = string.ascii_lowercase[:8]

for _ in range(int(input())):
    start = input()
    startw = int(start[1])
    starth = start[0]

    s = set()

    for w in boardw:
        if w != startw:
            s.add(starth + str(w))
    
    for h in boardh:
        if h != starth:
            s.add(h + str(startw))

    for square in s:
        print(square)