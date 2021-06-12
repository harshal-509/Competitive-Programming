#Author : harshal_509
import bisect
from collections import Counter
for _ in range(int(input())):
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    c=0
    m=0
    for i in range(n):
        q=bisect.bisect_right(a,r-a[i],lo=i+1)
        w=bisect.bisect_left(a,l-a[i],lo=i+1)
        c+=q-w
    print(c)
