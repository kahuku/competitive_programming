inp_string = input()
s1 = inp_string[0:len(inp_string)//3]
#print(s1)
s2 = inp_string[len(inp_string)//3: 2*len(inp_string)//3]
#print(s2)
s3 = inp_string[2*len(inp_string)//3:]
#print(s3)

if s1 == s2:
    print(s1)
elif s1 == s3:
    print(s1)
elif s2 == s3:
    print(s2)
