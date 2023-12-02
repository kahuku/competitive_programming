import numpy as np

def up(i, j):
    height = trees[i][j]
    visible = 0
    i -= 1
    while i >= 0:
        if trees[i][j] < height:
            visible += 1
        elif trees[i][j] >= height:
            visible += 1
            return visible
        i -= 1
    return visible

def down(i, j):
    height = trees[i][j]
    visible = 0
    i += 1
    while i < len(trees):
        if trees[i][j] < height:
            visible += 1
        elif trees[i][j] >= height:
            visible += 1
            return visible
        i += 1
    return visible

def left(i, j):
    height = trees[i][j]
    visible = 0
    j -= 1
    while j >= 0:
        if trees[i][j] < height:
            visible += 1
        elif trees[i][j] >= height:
            visible += 1
            return visible
        j -= 1
    return visible

def right(i, j):
    height = trees[i][j]
    visible = 0
    j += 1
    while j < len(trees[0]):
        if trees[i][j] < height:
            visible += 1
        elif trees[i][j] >= height:
            visible += 1
            return visible
        j += 1
    return visible

with open("advent_of_code2022/d8p1input.txt") as file:
    line = file.readline()

    trees = []

    while line != '':
        trees.append([int(char) for char in line.strip()])
        line = file.readline()
    
    trees = np.array(trees)

best = 0
for i in range(len(trees)):
    for j in range(len(trees[0])):
        score = up(i, j) * down(i, j) * left(i, j) * right(i, j)
        if score > best:
            best = score
print(best)