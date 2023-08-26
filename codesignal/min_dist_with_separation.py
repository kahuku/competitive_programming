# Roblox 2024 summer intern application
# given array of integers, return the minimum difference between any two elements with a separation of at least k
# separation is the distance between the two elements in the array

def solution(numbers, separation):
    numbers = [(numbers[i], i) for i in range(len(numbers))]
    numbers.sort()
    m = float('inf')
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j][1] - numbers[i][1] >= separation:
                m = min(m, abs(numbers[j][0] - numbers[i][0]))
                break
    return m