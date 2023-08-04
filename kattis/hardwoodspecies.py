from sys import stdin
lines = [line.strip() for line in stdin.readlines()]
trees = {}
total = 0
for line in lines:
    if line in trees:
        trees[line] += 1
    else:
        trees[line] = 1
    total += 1
for tree in sorted(trees):
    print(tree, "{:.5f}".format(trees[tree] / total * 100))