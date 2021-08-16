#Author:harshal_509
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    ans=1
    h={}
    m=l.copy()
    m.sort()
    for i in range(n):
        h[m[i]]=(i+1)
    for i in range(n-1):
        if(h[l[i]]+1==h[l[i+1]]):
            pass
        else:
            ans+=1
    if(k>=ans and k<=n):
        print("YES")
    else:
        print("NO")