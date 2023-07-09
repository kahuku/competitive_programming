s = input()
sequences = s.split('1')
longest = max(sequences, key=len)
print(int(len(longest) / 2) if len(longest) % 2 == 0 else int((len(longest) + 1) / 2))