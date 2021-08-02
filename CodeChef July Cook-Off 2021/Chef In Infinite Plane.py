#Author:koder_786
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    z=Counter(l)
    ans=0
    for i in z:
        ans+=min(z[i],i-1)
    print(ans)
