#I solve ? @danielpark
t = int(input())


for i in range(t):
    n, k = map(int, input().split())
    if n < 67:
        print(n)
    elif 67 <= n < 67**2:
        if k >= 1:
            a = n//67 + n%67 + 1
            print(a)
        else:
            print(n)
    elif 67**2 <= n < 67**3:
        if k == 1:
            a = 1 + n//67 + n%67
            print(a)
        elif k >= 2:
            a = 2 + n%67 + (n//67)%67 + n//67//67
            print(a)
        else:
            print(n)
    elif 67**3 <= n < 67**4:
        if k == 1: 
            a = 1 + n//67 + n%67
            print(a)
        elif k == 2:
            a = 2 + n%67 + (n//67)%67 + n//67//67
            print(a)
        elif k >= 3:
            a = 3 + n%67 + (n//67)%67 + ((n//67)//67)%67 + n//67//67//67
            print(a)
        else:
            print(n)