#Author:harshal_509
import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
from typing import DefaultDict
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    o=-1
    for i in range(n-1,-1,-1):
        if(l[i]==0):
            o=i
            break
    ans=[]
    for i in range(1,o+2):
        ans.append(i)
    ans.append(n+1)
    for i in range(o+2,n+1):
        ans.append(i)
    print(*ans)