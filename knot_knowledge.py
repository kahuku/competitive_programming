_ = input()
all = sorted([int(i) for i in input().split()])
learned = sorted([int(i) for i in input().split()])
missing = None
for i in range(len(learned)):
    if all[i] != learned[i]:
        missing = all[i]
        break
if missing == None:
    print(all[-1])
else:
    print(missing)
