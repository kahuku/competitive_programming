from sys import stdin
for line in stdin.readlines():
    name = []
    hrs = []
    for word in line.split():
        if word.replace('.', '').isnumeric(): hrs.append(float(word))
        else: name.append(word)
    print((sum(hrs) / len(hrs)), ' '.join(name))