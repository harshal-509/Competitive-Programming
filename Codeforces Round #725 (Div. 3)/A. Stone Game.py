#Author : harshal_509
import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=max(l)
    b=min(l)
    c=l.index(a)+1
    d=l.index(b)+1
    e=n-c+1
    f=n-d+1
    l=min(c+f,d+e,max(c,d),max(e,f))
    print(l)
