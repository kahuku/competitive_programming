cases = int(input())
for i in range(cases):
    num_fabrics = int(input())
    fabrics = []
    for _ in range(num_fabrics):
        inp = input().split()
        fabrics.append([inp[0], int(inp[1]), int(inp[2])])
    a = sorted(fabrics, key=lambda x: (x[0], x[2]))
    c = sorted(fabrics, key=lambda x: (x[1], x[2]))
    matches = 0
    for j, _ in enumerate(fabrics):
        if a[j] == c[j]:
            matches += 1
    print(f"Case #{i + 1}: {matches}")