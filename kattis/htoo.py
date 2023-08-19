from collections import defaultdict

def get_dict(molecule):
    d = defaultdict(int)
    for i in range(len(molecule)):
        if molecule[i].isalpha():
            char = molecule[i]
            if i == len(molecule) - 1:
                d[char] += 1
            else:
                if molecule[i + 1].isalpha():
                    d[char] += 1
                else:
                    num = 0
                    for j in range(i + 1, len(molecule)):
                        if molecule[j].isdigit():
                            num = num * 10 + int(molecule[j])
                        else:
                            break
                    d[char] += num
        else:
            continue
    return d

molecule, num = input().split()
num = int(num)
out_molecule = input()
molecule_dict = get_dict(molecule)
out_molecule_dict = get_dict(out_molecule)
out_num = float('inf')
for key in out_molecule_dict:
    if key not in molecule_dict:
        print(0)
        exit()
    out_num = min(out_num, (molecule_dict[key] * num) // out_molecule_dict[key])
print(out_num)