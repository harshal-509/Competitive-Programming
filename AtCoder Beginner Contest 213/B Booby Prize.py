#Author:koder_786
import math
n=int(input())
l=list(map(int,input().split()))
m=l.copy()
l.sort()
T=(l[-2])
print(m.index(T)+1)