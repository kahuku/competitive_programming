# Visa 2024 summer intern application

# given a starting rating and a list of changes to the rating, determine what category the player ends up in
def solve(rating, changes):
    rating += sum(changes)
    if rating < 1200:
        return "beginner"
    elif rating < 1500:
        return "intermediate"
    elif rating < 1800:
        return "advanced"
    elif rating < 2200:
        return "pro"