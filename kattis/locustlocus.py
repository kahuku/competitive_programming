def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

n = int(input())
t = []
for i in range(n):
    t.append(tuple(map(int, input().split())))
s = {compute_lcm(t[i][1], t[i][2]) + t[i][0] for i in range(n)}
s = sorted(s)
print(s[0])