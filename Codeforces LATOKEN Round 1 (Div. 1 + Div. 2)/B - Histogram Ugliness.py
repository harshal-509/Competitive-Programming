#Author: harshal_509
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if(n==1):
        print(l[0])
    else:
        u=l[0]
        for i in range(1,len(l)):
            u+=abs(l[i]-l[i-1])
        u+=l[-1]
        if(l[0]>l[1]):
            u-=abs(l[1]-l[0])
        for i in range(1,len(l)-1):
            if(l[i]>l[i-1] and l[i]>l[i+1]):
                u-=l[i]-max(l[i-1],l[i+1])
        if(l[-1]>l[-2]):
            u-=abs((l[-1])-(l[-2]))
        print(u)
