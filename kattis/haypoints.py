# RTE on last input -- not sure why
words, jobs = [int(i) for i in input().split()]
d = {}
for i in range(words):
    word, money = [i for i in input().split()]
    d[word] = int(money)
for i in range(jobs):
    line = input()
    sal = 0
    while line != ".":
        line = line.split()
        for word in line:
            if word in d:
                sal += d[word]
        line = input()
    print(sal)