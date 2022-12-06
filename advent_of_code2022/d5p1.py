#     [P]                 [C] [C]    
#     [W]         [B]     [G] [V] [V]
#     [V]         [T] [Z] [J] [T] [S]
#     [D] [L]     [Q] [F] [Z] [W] [R]
#     [C] [N] [R] [H] [L] [Q] [F] [G]
# [F] [M] [Z] [H] [G] [W] [L] [R] [H]
# [R] [H] [M] [C] [P] [C] [V] [N] [W]
# [W] [T] [P] [J] [C] [G] [W] [P] [J]
#  1   2   3   4   5   6   7   8   9 

stacks = [
    ['W', 'R', 'F'],
    ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'],
    ['P', 'M', 'Z', 'N', 'L'],
    ['J', 'C', 'H', 'R'],
    ['C', 'P', 'G', 'H', 'Q', 'T', 'B'],
    ['G', 'C', 'W', 'L', 'F', 'Z'],
    ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C'],
    ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C'],
    ['J', 'W', 'H', 'G', 'R', 'S', 'V']
]

with open("advent_of_code2022/d5p1input.txt") as file:
    line = file.readline()

    while line != '':
        line = line.split()
        n, start, finish = int(line[1]), int(line[3]) - 1, int(line[5]) - 1

        for _ in range(n):
            crate = stacks[start].pop()
            stacks[finish].append(crate)

        line = file.readline()
    
    print(''.join([stack.pop() for stack in stacks]))