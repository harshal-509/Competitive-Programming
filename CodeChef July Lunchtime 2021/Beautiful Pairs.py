#Author:koder_786
import math
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    z=Counter(l)
    ans=0
    for i in z:
        ans+=(n-z[i])*z[i]
    print(ans)
