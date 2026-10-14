moves = []
d = [0]*301

def correcting(a, x):
    if (x==1):
        return
    i = d[x]
    while (i >= x):
        d[x], d[a[i-x]] = d[a[i-x]], d[x]
        a[i], a[i-x] = a[i-x], x
        moves.append([i+1, i-x+1])
        i-=x
    correcting(a, x-1)

n = int(input())

a = [int(_) for _ in input().split()]
for i in range(n):
    d[a[i]] = i
for i in range(n+1):
    correcting(a, i)
correcting(a,1)
print(len(moves))
for _ in moves:
    print(*_)
