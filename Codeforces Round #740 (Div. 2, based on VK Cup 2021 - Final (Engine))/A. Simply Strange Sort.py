#Author:harshal_509
import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=sorted(l)
    count=0
    while(a!=l):
        if(count%2==0):
            for j in range(n-1):
                if(j%2==0):
                    if(l[j]>l[j+1]):
                        l[j],l[j+1]=l[j+1],l[j] 
        else:
            for j in range(n-1):
                if(j%2==1):
                    if(l[j]>l[j+1]):
                        l[j],l[j+1]=l[j+1],l[j] 
        count+=1 
    print(count)