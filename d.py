for t in range(int(input())):
    n = int(input())
    p = sorted([int(_) for _ in input().split()])
    mn = 0
    for i in range(n):
        mn = max(mn, p[i]+p[-i-1])
    print(mn, p[-1]+p[-2])
    