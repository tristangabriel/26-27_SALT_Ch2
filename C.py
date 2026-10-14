n, b = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

mx = max(a)
if (mx>=0):
    for i in a:
        if (i>0):
            b+=i
elif (mx<0 and mx+b>=0):
    b = mx+b
else:
    b=-1

print(b)