articles, impact = [int(i) for i in input().split()]
print(articles * (impact - 1) + 1)