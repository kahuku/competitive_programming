line_length = int(input()) - 1
places = [int(i) for i in input().split()]
sorted_places = sorted(places)
line = ['1']
[line.append(str(places.index(sorted_place) + 2)) for sorted_place in sorted_places]
print(' '.join(line))