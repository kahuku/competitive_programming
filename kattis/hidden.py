password, text = map(list, input().split())
orders = [set(password[i:]) for i in range(len(password))]
password_index = 0
valid = True
for i in range(len(text)):
    if text[i] == password[password_index]:
        password_index += 1
    elif text[i] in orders[password_index]:
        valid = False
        break
    if password_index == len(password):
        break

print('PASS' if valid and password_index == len(password) else 'FAIL')