#Author : harshal_509
from math import gcd
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    o=[]
    e=[]
    for i in range(len(l)):
        if(l[i]%2!=0):
            o.append(l[i])
        else:
            e.append(l[i])
    a=0
    o.sort()
    l=e+o
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(gcd(l[i],2*l[j])>1):
                a+=1
    print(a)