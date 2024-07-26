o = []
for c in input():
    if c in 'aeiouyAEIOUY':
        o.append(c)
print(''.join(o))

# interestingly enough, doing this with string concatenation (o = ''; o += c) will result in a TLE