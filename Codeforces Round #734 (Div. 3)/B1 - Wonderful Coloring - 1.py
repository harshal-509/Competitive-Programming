#Author:harshal_509
import math
from collections import Counter
for _ in range(int(input())):
    s=input()
    h={}
    ans=0
    for i in range(97,123):
        h[chr(i)]=0
    for i in range(len(s)):
        if(h[s[i]]<2):
            h[s[i]]+=1
            ans+=1
    print(ans//2)