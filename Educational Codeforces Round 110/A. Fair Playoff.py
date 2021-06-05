#Author : harshal_509
for i in range(int(input())):
    l=list(map(int,input().split()))
    a=max(l[0],l[1])
    b=max(l[2],l[3])
    l.sort()
    if(a+b==l[2]+l[3]):
        print("YES")
    else:
        print("NO")