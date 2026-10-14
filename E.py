n = int(input())
g = list(map(int, input().split()))
a = ""

a += ("U"*g[0])
a += ("R")

for i in range(n-1):
    if g[i] > g[i+1]:
        a += ("D"*(abs(g[i]-g[i+1])))
        a += ("R")
    elif g[i] == g[i+1]:
        a += ("R")
    else:
        a += ("U"*abs(g[i]-g[i+1]))
        a += ("R")

a += ("D"*g[-1])
a += ("L"*n)

print(a)