inp = input().split()
left_tines = int(inp[0])
right_tines = int(inp[1])

if left_tines == 0 and right_tines == 0:
    print("Not a moose")
elif left_tines == right_tines:
    print("Even ", left_tines * 2)
elif left_tines < right_tines:
    print("Odd ", right_tines * 2)
elif left_tines > right_tines:
    print("Odd ", left_tines * 2)
