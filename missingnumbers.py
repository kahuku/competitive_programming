num_nums = int(input())
arr = []
for i in range(num_nums):
    arr.append(int(input()))
arr.sort()
missed = []
for i in range(1, arr[-1]):
    if i not in arr:
        missed.append(i)
if len(missed) > 0:
    [print(i) for i in missed]
else:
    print("good job")