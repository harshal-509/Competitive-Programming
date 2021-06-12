#Author : harshal_509
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    if(s%n!=0):
        print("-1")
    else:
        t=s//n
        a=0
        for i in l:
            if(i>t):
                a+=1
        print(a)
