n_ingredients, n_recipes = map(int, input().split())
ingredients = list(map(int, input().split()))
recipes = [[int(i) for i in input().split()] for _ in range(n_recipes)]
profit = 0
for recipe in recipes:
    cost = recipe[-1]
    recipe = recipe[:-1]
    minimum_ingredient = float('inf')
    for i in range(n_ingredients):
        if recipe[i] == 0: continue
        minimum_ingredient = min(minimum_ingredient, int(ingredients[i] / recipe[i]))
    profit = max(profit, minimum_ingredient * cost)
print(profit)