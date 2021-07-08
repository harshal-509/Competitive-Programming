#Author:harshal_509
import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=sum(l)
    if(ans%n==0):
        print(0)
    else:
        m=ans%n
        print(m*(n-m))