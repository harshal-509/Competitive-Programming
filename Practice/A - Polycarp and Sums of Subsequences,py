#Author:harshal_509
from collections import *
for i in range(int(input())):
    l=list(map(int,input().split()))
    l.sort()
    n=6
    flag=0
    for i in range(n-1):
        for j in range(i+1,n-1):
            for k in range(j+1,n-1):
                if(l[i]+l[j]+l[k]==l[-1]):
                    flag=1
                    print(l[i],l[j],l[k])
                    break
            if(flag):
                break
        if(flag):
            break
