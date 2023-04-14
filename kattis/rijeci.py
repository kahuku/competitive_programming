n = int(input())
num_a, num_b = 1, 0
for i in range(1, n + 1):
    new_ba = num_b
    new_b = num_a
    num_a = new_ba
    num_b = new_b + new_ba
print(num_a, num_b)