def p(s):
    bag=[]
    li = input()
    for i in range(len(s)):
        if li[i]=="*":
            bag.append(s[i])
    return bag

bag = set(p("QWERTYUIOP")+p("ASDFGHJKL")+p("ZXCVBNM"))
for _ in range(int(input())):
    li = input()
    if set(list(li))!=bag:
        print("IM", end='')
    print("POSSIBLE")

    