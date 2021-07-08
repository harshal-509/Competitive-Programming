#Author:harshal_509
import math
for _ in range(int(input())):
    m,n=map(int,input().split())
    ans=abs(m-n)
    if(m==n):
        print(0,0)
    else:
        h=n//ans
        if(h*ans!=n and abs((h+1)*ans-n)<abs(h*ans-n)):
            h+=1
        print(ans,abs(n-(h*ans)))