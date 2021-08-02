#Author:koder_786
import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    e,o=[],[]
    for i in range(n):
        if(l[i]%2==0):
            e.append(l[i])
        else:
            o.append(l[i])
    e.sort()
    o.sort()
    if(len(e)>len(o)):
        ans=e[0]
        for i in range(n):
            l[i]^=ans
        ans1=l[0]
        for i in range(1,n):
            ans1|=l[i]
        print(ans,ans1)
    else:
        ans=o[0]
        for i in range(n):
            l[i]^=ans
        ans1=l[0]
        for i in range(1,n):
            ans1|=l[i]
        print(ans,ans1)