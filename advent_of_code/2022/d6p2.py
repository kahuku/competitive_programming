from queue import Queue

with open("advent_of_code2022/d6p1input.txt") as file:
    transmission = file.readline()

    q = Queue(maxsize=14)
    for i, char in enumerate(transmission):
        q.put(char)
        if q.full():
            s = set(q.queue)
            if len(s) == 14:
                print(i + 1)
                exit()
            q.get()
