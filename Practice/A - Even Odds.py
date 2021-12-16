#Author:harshal_509
from math import *
for _ in range(1):
    l = list(map(int, input().split()))
    n=l[0]
    k=l[1]
    if(n%2==0):
        if(k<=n//2):
            print(1+(k-1)*2)
        else:
            k=k%(n//2)
            if(k==0):
                k=n//2
            print(2+(k-1)*2)
    else:
        if(k<=n//2+1):
            print(1+(k-1)*2)
        else:
            k=k%(n//2+1)
            if(k==0):
                k=n//2+1
            print(2+(k-1)*2)
