#Author:koder_786
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    t=min(l)
    z=Counter(l)
    flag=1
    for i in range(n):
        if(l[i]==t or (l[i]%(l[i]-t))==t):
            pass
        else:
            flag=0
    if(flag):
        print(n-z[t])
    else:
        print(n)
