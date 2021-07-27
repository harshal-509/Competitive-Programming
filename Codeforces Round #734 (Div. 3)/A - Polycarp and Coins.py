#Author:harshal_509
import math
for _ in range(int(input())):
    n=int(input())
    x=math.ceil(n/3)
    y=n-x*2
    if(x-y==2):
        print(y+2,x-1)
    else:
        print(y,x)