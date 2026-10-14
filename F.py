
ans=[]

def trying(n, g): #code in E
    a=''
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
    return a

def sol(s):
    x,y=0,0
    for j in range(len(s)):
        i = s[j]
        if (i=='U'):
            y+=1
        elif (i=='R'):
            ans.append(y)
            x+=1
        elif (i=='D'):
            if (j==0):
                return 0
            if (s[j-1]=='U'):
                return 0
            y-=1
        elif (i=='L'):
            if (y!=0):
                return 0
            x-=1

        if (x<0 and y<0):
            return 0
        if (y==0):
            if s[j+1:]==("L"*x):
                return 1
            return 0

s = input()
if sol(s) and trying(len(ans), ans)==s: #check if true and matching
    print(len(ans))
    print(*ans)
else:
    print("IMPOSSIBLE")
    