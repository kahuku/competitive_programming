ciphertext = input()
mid = len(ciphertext) // 2
left = ciphertext[:mid]
right = ciphertext[mid:]
left_sum = sum(ord(c) - ord('A') for c in left)
right_sum = sum(ord(c) - ord('A') for c in right)
left = ''.join(chr((ord(c) - ord('A') + left_sum) % 26 + ord('A')) for c in left)
right = ''.join(chr((ord(c) - ord('A') + right_sum) % 26 + ord('A')) for c in right)
result = ''.join(chr((ord(left[i]) - ord('A') + ord(right[i]) - ord('A')) % 26 + ord('A')) for i in range(mid))
print(result)