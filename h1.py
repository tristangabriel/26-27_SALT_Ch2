moves = []

d = [0]*301
a=[]

def swap(i, j):
    moves.append([i+1, j+1])
    d[a[i]], d[a[j]] = d[a[j]], d[a[i]]
    a[i], a[j] = a[j], a[i]

def solve(n):
    while (d[2] < d[n] and d[2]<n-2):
        swap(d[2], d[2]+2)
    while (d[2] > d[n]+2):
        swap(d[2], d[2]-2)
    while (d[1] < d[n]):
        swap(d[1], d[1]+1)
    while (d[1] > d[n]+1):
        swap(d[1], d[1]-1)

    swap(d[2], d[n])
    while (d[n]<n-1):
        swap(d[1], d[2])
        swap(d[2], d[n]+1)
        swap(d[1], d[1]+1)
        swap(d[1], d[n])
        swap(d[2], d[n])

n = int(input())
a = [int(_) for _ in input().split()]
for i in range(n):
    d[a[i]] = i
for i in range(n, 2, -1):
    solve(i)
moves.append([1, 2])
print(len(moves))
for _ in moves:
    print(*_)