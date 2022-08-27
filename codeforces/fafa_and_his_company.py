employees = int(input())
print(sum(employees % i == 0 for i in range(1, employees)))