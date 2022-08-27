CALS_PER_BOTTLE = 400

cases = int(input())
for _ in range(cases):
    required_cals = int(input())
    bottles = required_cals // CALS_PER_BOTTLE
    if required_cals % CALS_PER_BOTTLE != 0:
        bottles += 1
    print(bottles)