n = int(input())
cases = []
for i in range(n):
    cases.append(input())
d = {
    'vac_a': 0,
    'vac_b': 0,
    'vac_c': 0,
    'con_a': 0,
    'con_b': 0,
    'con_c': 0
}
vaccinated = 0
control = 0
for case in cases:
    if case[0] == 'Y':
        vac = 'vac_'
        vaccinated += 1
    else:
        vac = 'con_'
        control += 1
    if case[1] == 'Y':
        d[vac + 'a'] += 1
    if case[2] == 'Y':
        d[vac + 'b'] += 1
    if case[3] == 'Y':
        d[vac + 'c'] += 1
a = (1 - (d['vac_a'] / vaccinated) / (d['con_a'] / control)) * 100
b = (1 - (d['vac_b'] / vaccinated) / (d['con_b'] / control)) * 100
c = (1 - (d['vac_c'] / vaccinated) / (d['con_c'] / control)) * 100
print(a if a > 0 else 'Not Effective')
print(b if b > 0 else 'Not Effective')
print(c if c > 0 else 'Not Effective')