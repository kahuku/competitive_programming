from collections import defaultdict, deque
start = input()
d = defaultdict(list)
for _ in range(int(input())):
    a, b = input().split(' -> ')
    d[a].append(b)

q = deque()
q.append((start, [start]))
while q:
    person, path = q.popleft()
    if person == 'Neil Armstrong':
        for p in path[::-1]:
            print(p)
        exit()
    for p in d[person]:
        q.append((p, path + [p]))