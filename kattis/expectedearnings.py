nums = [float(i) for i in input().split()]
n, k, p = nums[0], nums[1], nums[2]

gain = n * p
if gain < k:
    print("spela")
else:
    print("spela inte!")
