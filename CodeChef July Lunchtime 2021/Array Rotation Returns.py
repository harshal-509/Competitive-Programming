#Author:koder_786
import math
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=a[0]
    p=-1
    re=1000000000000000
    for i in range(n):
        r=(b[i%n]+x)%n
        if(re>r):
            re=r
            p=i%n
        elif(re==r):
            i1=0
            i2=i%n
            p1=p%n
            for j in range(n//2):
                if((a[i1%n]+b[i2%n])%n==(a[i1%n]+b[p1%n])%n):
                    i1+=1
                    i1= i1%n
                    i2+=1
                    p1+=1
                    p1 = p1%n
                    i2 = i2%n
                else:
                    break
            if((a[i1%n]+b[i2%n])%n<(a[i1%n]+b[p1%n])%n):
                p=i%n
    k=p%n
    for i in range(n):
        k=k%n
        print((b[k%n]+a[i%n])%n,end=" ")
        k+=1
