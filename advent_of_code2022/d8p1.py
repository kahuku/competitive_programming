import numpy as np

def thingy():
    for i, row in enumerate(trees):
        height = -1
        for j, tree in enumerate(row):
            if tree > height:
                height = tree
                visible[i][j] = True

with open("advent_of_code2022/d8p1input.txt") as file:
    line = file.readline()

    trees = []

    while line != '':
        trees.append([int(char) for char in line.strip()])
        line = file.readline()
    
    trees = np.array(trees)

    visible = [[False for _ in range(len(trees[0]))] for _ in range(len(trees))]

    thingy()
    trees, visible = np.transpose(trees), np.transpose(visible)
    thingy()
    trees, visible = np.fliplr(np.flipud(trees)), np.fliplr(np.flipud(visible))
    thingy()
    trees, visible = np.transpose(trees), np.transpose(visible)
    thingy()

    # print(visible)
    print(np.count_nonzero(visible))
