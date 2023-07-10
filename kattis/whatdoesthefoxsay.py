for _ in range(int(input())):
    words = input().split()
    sounds = set()
    while True:
        line = input()
        if line == 'what does the fox say?':
            break
        else:
            animal_sound = line.split()[-1]
            sounds.add(animal_sound)
    fox_sounds = [word for word in words if word not in sounds]
    print(' '.join(fox_sounds))