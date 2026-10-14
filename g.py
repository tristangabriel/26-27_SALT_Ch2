n = int(input())
a = [int(_) for _ in input().split()]

c = 0
sm = a[0]

for i in range(1, n):
    c += a[i]*sm
    sm += a[i]

print(sm, c)
