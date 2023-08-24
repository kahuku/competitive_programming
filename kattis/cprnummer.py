cpr = ''.join(input().split('-'))
s = int(cpr[0]) * 4 + int(cpr[1]) * 3 + int(cpr[2]) * 2 + int(cpr[3]) * 7 + int(cpr[4]) * 6 + int(cpr[5]) * 5 + int(cpr[6]) * 4 + int(cpr[7]) * 3 + int(cpr[8]) * 2 + int(cpr[9])
print(int(s % 11 == 0))