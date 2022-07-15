starting_num = int(input())
line = []
for i in range(starting_num):
    line.append(input())

changes = int(input())
for i in range(changes):
    action = input().split()
    
    if action[0] == 'cut':
        index = line.index(action[2])
        line.insert(index, action[1])
        
    elif action[0] == 'leave':
        line.remove(action[1])

for i in line:
    print(i)
