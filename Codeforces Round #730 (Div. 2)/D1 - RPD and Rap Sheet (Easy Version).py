#Author:harshal_509
import sys
for _ in range(int(input())):
    n,k=map(int,input().split())
    y=0
    for i in range(n):
        y=i^(i-1)
        print(max(y,0))
        sys.stdout.flush()
        r=int(input())
        if(r==1):
            break