#Author:koder_786
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def dfs(node,s):
    s.add(node)    
    print(node,end=" ")
    for i in d[node]:
        if(i not in s):
            dfs(i,s)
            print(node,end=" ")
d=defaultdict(list)
for _ in range(int(input())-1):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
s=set()
for i in d:
    d[i]=sorted(d[i])
dfs(1,s)