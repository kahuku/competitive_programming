inp = input().split()
golds = int(inp[0])
silvers = int(inp[1])
coppers = int(inp[2])

buyingPower = 0
buyingPower += 3 * golds + 2 * silvers + coppers
#print(buyingPower)

to_print = []
if buyingPower >= 8:
    to_print.append("Province")
elif buyingPower >= 5:
    to_print.append("Duchy")
elif buyingPower >= 2:
    to_print.append("Estate")

if buyingPower >= 6:
    to_print.append("Gold")
elif buyingPower >= 3:
    to_print.append("Silver")
else:
    to_print.append("Copper")

if len(to_print) == 1:
    print(to_print[0])
else:
    print(to_print[0] + " or " + to_print[1])
