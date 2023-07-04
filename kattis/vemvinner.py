rows = [''.join(input().split()) for _ in range(3)]
if 'XXX' in rows[0] or 'XXX' in rows[1] or 'XXX' in rows[2]:
    print('Johan har vunnit')
elif 'OOO' in rows[0] or 'OOO' in rows[1] or 'OOO' in rows[2]:
    print('Abdullah har vunnit')
elif rows[0][1] == rows[1][1] == rows[2][1] == 'X' or rows[0][0] == rows[1][0] == rows[2][0] == 'X' or rows[0][2] == rows[1][2] == rows[2][2] == 'X':
    print('Johan har vunnit')
elif rows[0][1] == rows[1][1] == rows[2][1] == 'O' or rows[0][0] == rows[1][0] == rows[2][0] == 'O' or rows[0][2] == rows[1][2] == rows[2][2] == 'O':
    print('Abdullah har vunnit')
elif rows[0][0] == rows[1][1] == rows[2][2] == 'X' or rows[0][2] == rows[1][1] == rows[2][0] == 'X':
    print('Johan har vunnit')
elif rows[0][0] == rows[1][1] == rows[2][2] == 'O' or rows[0][2] == rows[1][1] == rows[2][0] == 'O':
    print('Abdullah har vunnit')
else:
    print('ingen har vunnit')