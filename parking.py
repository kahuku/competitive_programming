num_cases = int(input())
for i in range(num_cases):
    num_stores = int(input())
    store_pos = input().split()
    store_pos = [int(i) for i in store_pos]
    store_pos.sort()
    diff = store_pos[len(store_pos) - 1] - store_pos[0]
    print(diff * 2)
