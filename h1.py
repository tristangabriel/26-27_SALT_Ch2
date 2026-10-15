moves = []

d = [0]*301
a=[]

def swap(i, j):
    moves.append([i+1, j+1])
    d[a[i]], d[a[j]] = d[a[j]], d[a[i]]
    a[i], a[j] = a[j], a[i]


# abuse 1 and 2 by passing n around until the very end, then do solve(n-1)
def solve(n):
    #brings it into "...n 1 2..."
    while (d[2] < d[n] and d[2]<n-2):
        swap(d[2], d[2]+2)
    while (d[2] > d[n]+2):
        swap(d[2], d[2]-2)
    while (d[1] < d[n]):
        swap(d[1], d[1]+1)
    while (d[1] > d[n]+1):
        swap(d[1], d[1]-1)
    while (d[2] < d[n] and d[2]<n-2):
        swap(d[2], d[2]+2)

    #turns it into ...2 1 n
    swap(d[2], d[n])
    while (d[n]<n-1):
        swap(d[1], d[2])
        swap(d[2], d[n]+1)
        swap(d[1], d[1]+1)
        swap(d[1], d[n])
        #loops back into "...n 1 2...", but 1 element rightward now
        swap(d[2], d[n])

n = int(input())
a = [int(_) for _ in input().split()]

for i in range(n):
    d[a[i]] = i

for i in range(n, 2, -1):  #stop at 3
    solve(i)
moves.append([1, 2]) #fix "2 1 3 4...n"
print(len(moves))
for _ in moves:
    print(*_)