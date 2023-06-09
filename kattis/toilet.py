s = input()

ans_up = 0
ans_down = 0
ans_pref = 0
curr_up = s[0]
curr_down = s[0]

for i in range(1, len(s)):
    if curr_up == 'D':
        ans_up += 1
    elif curr_up == 'U' and s[i] == 'D':
        ans_up += 2
    curr_up = 'U'
    
    if curr_down == 'U':
        ans_down += 1
    elif curr_down == 'D' and s[i] == 'U':
        ans_down += 2
    curr_down = 'D'
    
    if s[i - 1] != s[i]:
        ans_pref += 1

print(ans_up)
print(ans_down)
print(ans_pref)