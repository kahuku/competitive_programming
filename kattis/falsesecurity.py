from sys import stdin
lines = stdin.readlines()
morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', \
            'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', \
            'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', \
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', \
            'X': '-..-', 'Y': '-.--', 'Z': '--..', '_': '..--', '.': '---.', \
            ',': '.-.-', '?': '----'}
morse_rev = {v: k for k, v in morse.items()}
for line in lines:
    line = line.strip()
    morse_code = ''
    lens = []
    for c in line:
        morse_code += morse[c]
        lens.append(len(morse[c]))
    lens = lens[::-1]
    i = 0
    c = 0
    ans = ''
    while i < len(morse_code):
        ans += morse_rev[morse_code[i:i+lens[c]]]
        i += lens[c]
        c += 1
    print(ans)
