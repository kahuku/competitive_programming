def div(rating):
    if rating >= 1900:
        return '1'
    elif rating >= 1600:
        return '2'
    elif rating >= 1400:
        return '3'
    else:
        return '4'

[print("Division", div(int(input()))) for _ in range(int(input()))]