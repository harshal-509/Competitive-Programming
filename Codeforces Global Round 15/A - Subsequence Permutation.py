#Author:harshal_509
import math
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    s=input()
    ans=0
    t=sorted(s)
    for i in range(n):
        if(t[i]!=s[i]):
            ans+=1
    print(ans)