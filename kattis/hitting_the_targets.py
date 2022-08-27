num_targets = int(input())

target_list = []
for target in range(num_targets):
    target_list.append(input())

target_coords = []
for target in target_list:
    s = target.split(' ')
    target_type = s[0]
    if target_type == "rectangle":
        x1, y1, x2, y2 = int(s[1]), int(s[2]), int(s[3]), int(s[4])
        target_coords.append([x1, y1, x2, y2])
    if target_type == "circle":
        x, y, r = int(s[1]), int(s[2]), int(s[3])
        target_coords.append([x, y, r])

num_shots = int(input())

shots_list = []
for shot in range(num_shots):
    shots_list.append(input())

shot_coords = []
for shot in shots_list:
    s = shot.split(' ')
    shot_coords.append([int(s[0]), int(s[1])])

for shot in shot_coords:
    targets_hit = 0
    i = 0
    for i in range(len(target_coords)):
        if target_list[i].split(' ')[0] == "rectangle":
            if shot[0] >= target_coords[i][0] and shot[0] <= target_coords[i][2]:
                if shot[1] >= target_coords[i][1] and shot[1] <= target_coords[i][3]:
                    targets_hit += 1
        else:
            circleY = target_coords[i][1]
            shotY = shot[1]
            circleX = target_coords[i][0]
            shotX = shot[0]
            
            dist = ((circleX - shotX)**2 + (circleY - shotY)**2)**0.5
            if dist <= target_coords[i][2]:
                targets_hit += 1
            
        i += 1
    print(targets_hit)
