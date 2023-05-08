from sys import stdin

d = {
    "Ab": "G#",
    "G#": "Ab",
    "A#": "Bb",
    "Bb": "A#",
    "C#": "Db",
    "Db": "C#",
    "D#": "Eb",
    "Eb": "D#",
    "F#": "Gb",
    "Gb": "F#"
}

for i, line in enumerate(stdin.readlines()):
    k, m = line.split()
    if k in d:
        print(f"Case {i + 1}: {d[k]} {m}")
    else:
        print(f"Case {i + 1}: UNIQUE")