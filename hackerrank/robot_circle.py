# Goldman Sachs 2024 summer intern app
# given list of strings of robot commands, determine if robot is going in a circle if it continues indefinitely

def isCircle(commands):
    out = []
    for command_list in commands:
        if isCircleHelper(command_list):
            out.append("YES")
        else:
            out.append("NO")
    return out

def isCircleHelper(commands):
    directions = ['U', 'R', 'D', 'L']
    start_pos = [0, 0, 'U']
    pos = start_pos
    times = 10
    for time in times:
        for command in commands:
            curr_dir = pos[2]
            if command == 'G':
                if curr_dir == 'U':
                    pos[1] += 1
                elif curr_dir == 'R':
                    pos[0] += 1
                elif curr_dir == 'D':
                    pos[1] -= 1
                elif curr_dir == 'L':
                    pos[0] -= 1
            elif command == 'L':
                next_dir = directions[(directions.index(curr_dir) - 1)]
                pos[2] = next_dir
            elif command == 'R':
                next_dir = directions[(directions.index(curr_dir) + 1) % 4]
                pos[2] = next_dir
        if pos == start_pos:
            return True
    return False
    
