s = input()
print(chr(int(sum([ord(c) for c in s]) / len(s))))