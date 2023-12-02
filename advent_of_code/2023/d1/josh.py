from sys import stdin

def rls():
    return [line.strip() for line in stdin.readlines()]
o=[]
d={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
for line in rls():
    f=None
    l=None
    for i in range(len(line)):
        for k in d:
            if line[i:i+len(k)]==k:
                l=str(d[k])
                if f==None:
                    f=str(d[k])
                
        if ord('0') <=ord(line[i]) <= ord('9'):
            l=line[i]
            if f==None:
                f=line[i]
    print(f, l)
    o.append(int(f+l))
print(sum(o))