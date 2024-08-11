r, c = map(int, input().split())
g = [list(input().replace('.', '')) for _ in range(r)]
print(''.join([''.join(x) for x in g if len(x) > 0]))