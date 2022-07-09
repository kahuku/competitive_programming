inp = float(input())
ans = round(inp / 100)
if inp % 100 == 49:
    ans += 1
if ans < 1:
    ans = 1
print (ans * 100 - 1)
