n, m = map(int, input().split())
a = input()
l = []

def count(a):
    sm = 0
    for i in a:
        if i in "TJQK":
            sm+=10
        elif i=='A':
            sm+=1
        elif i!='*':
            sm += int(i)

def solve(d, m, n):

    ans = list(d)
    sm = count(d)
    jok= d.count('*')

    if (sm+jok > m):  # minimum joker is A
        return "NO"
    elif (sm+jok*10<m): #maximum is a 10
        return "NO"
    
    m-= jok+sm

    # make all joker -> ace, then fill up greedily
    for i in range(n):
        if d[i]=='*':
            if m>=9:
                ans[i]='T'
                m-=9
            elif m>0:
                ans[i]=str(m+1)
                m=0
            else:
                ans[i]='A'

    return "YES\n"+"".join(ans)

print(solve(a, m, n))
    