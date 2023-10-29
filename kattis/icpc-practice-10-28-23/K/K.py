from sys import stdin

lines = stdin.readlines()
d1names = {}
d2names = {}
lower_to_orig1n = {}
lower_to_orig2n = {}
lower_to_orig1e = {}
lower_to_orig2e= {}

found = False
for i in range(len(lines)):
    line = lines[i]
    if line == '\n':
        found = True
        continue
    elif not found:
        a, b, email = line.split()
        name = a + " " + b

        lower_to_orig1n[email.lower()] = name.lower()
        lower_to_orig1e[name.lower()] = email.lower()

        d1names[email] = name

    else:
        a, b, email = line.split()
        name = a + " " + b

        lower_to_orig2n[email.lower()] = name.lower()
        lower_to_orig2e[name.lower()] = email.lower()

        d2names[email] = name


out = []

for email, name in sorted(d1names.items(), key=lambda x: x[0].lower()):
    if name.lower() not in lower_to_orig2e and email.lower() not in lower_to_orig2n:
        out.append(f"I {email} {name.split()[1]} {name.split()[0]}")

for email, name in sorted(d2names.items(), key=lambda x: x[0].lower()):
    if name.lower() not in lower_to_orig1e and email.lower() not in lower_to_orig1n:
        out.append(f"O {email} {name.split()[1]} {name.split()[0]}")

if len(out) > 0:
    for line in out:
        print(line)
else:
    print("No mismatches.")