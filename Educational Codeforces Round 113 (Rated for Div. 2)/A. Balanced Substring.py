#Author:harshal_509
import math
for _ in range(int(input())):
    n=int(input())
    s=input()
    n=len(s)
    flag=0
    for i in range(1,n):
        if(s[i]!=s[i-1]):
            print(i,i+1)
            flag=1
            break
    if(flag):
        pass
    else:
        print(-1,-1)