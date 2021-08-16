#Author:harshal_509
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    a=max(l)
    a=(sum(l[:n-1]))/(n-1)
    b=l[-1]
    print('%.6f'%(a+b))