#Author:harshal_509
import math
mod=int(1e9+7)
for _ in range(int(input())):
    n=int(input())
    c=n
    ans=0
    j,i=1,1
    while(1):
        j=(j*i)//math.gcd(j,i)
        ans=((ans%mod)+((c-(n//j)%mod)*((i)%mod))%mod)%mod
        c=n//j
        i+=1
        if(c==0):
            break
    print(ans)