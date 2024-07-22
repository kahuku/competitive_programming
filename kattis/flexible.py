w, p = map(int, input().split())
partitions = [0]
partitions += list(map(int, input().split()))
partitions.append(w)
widths = set()
for i in range(len(partitions)):
    for j in range(i+1, len(partitions)):
        widths.add(partitions[j] - partitions[i])
print(' '.join(map(str, sorted(widths))))