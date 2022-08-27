import sys
input_string = input()

i = 0
for i in range(len(input_string)):
    if i != 0:
        if input_string[i] in input_string[0:i] or input_string[i] in input_string[i+1:len(input_string)-1]:
            print("0")
            sys.exit()
    else:
        if input_string[i] in input_string[1:len(input_string)-1]:
            print("0")
            sys.exit()
    i += 1
print("1")
