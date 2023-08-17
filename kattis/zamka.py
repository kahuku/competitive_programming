import threading

def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def find_min_range(min_value, max_value, target_value, result_min):
    for i in range(min_value, max_value + 1):
        if digit_sum(i) == target_value:
            result_min.append(i)
            break

def find_max_range(min_value, max_value, target_value, result_max):
    for i in range(max_value, min_value - 1, -1):
        if digit_sum(i) == target_value:
            result_max.append(i)
            break

def main():
    min_value = int(input())
    max_value = int(input())
    target_value = int(input())

    result_min = []
    result_max = []

    threads = []

    min_thread = threading.Thread(target=find_min_range, args=(min_value, max_value, target_value, result_min))
    max_thread = threading.Thread(target=find_max_range, args=(min_value, max_value, target_value, result_max))

    threads.append(min_thread)
    threads.append(max_thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(result_min[0])
    print(result_max[0])

if __name__ == "__main__":
    main()
