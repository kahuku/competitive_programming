words = input().split()
count = sum(1 for word in words if 'ae' in word)
print('dae ae ju traeligt va' if count / len(words) >= 0.4 else 'haer talar vi rikssvenska')