attributes = input().split()
n = int(input())
songs = []
for _ in range(n):
    songs.append(input().split())
n = int(input())
for _ in range(n):
    field = input()
    songs.sort(key=lambda song: song[attributes.index(field)])
    print(' '.join(attributes))
    for song in songs:
        print(' '.join(song))
    print()
