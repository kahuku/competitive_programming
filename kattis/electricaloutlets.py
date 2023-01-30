n = int(input())
for _ in range(n):
    num_strips, *plug_array = [int(i) for i in input().split()]
    plug_array.insert(0, 1)
    print(sum([strip - 1 if i != len(plug_array) - 1 else strip for i, strip in enumerate(plug_array)]))