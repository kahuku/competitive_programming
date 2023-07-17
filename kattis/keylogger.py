d = {'clank': 'a', 'bong': 'b',
        'click': 'c', 'tap': 'd',
        'poing': 'e', 'clonk': 'f',
        'clack': 'g', 'ping': 'h',
        'tip': 'i', 'cloing': 'j',
        'tic': 'k', 'cling': 'l',
        'bing': 'm', 'pong': 'n',
        'clang': 'o', 'pang': 'p',
        'clong': 'q', 'tac': 'r',
        'boing': 's', 'boink': 't',
        'cloink': 'u', 'rattle': 'v',
        'clock': 'w', 'toc': 'x',
        'clink': 'y', 'tuc': 'z',
        'whack': ' '}

s = ''
shift = False
for _ in range(int(input())):
    key = input()
    if key == 'dink':
        shift = not shift
    elif key == 'thumb':
        shift = not shift
    elif key == 'bump':
        shift = not shift
    elif key == 'pop':
        s = s[:-1]
    else:
        s += d[key] if not shift else d[key].upper()
print(s)