for _ in range(int(input())):
    input()
    l = list(map(int, input().split()))
    print(sum([candies - min(l) for candies in l]))