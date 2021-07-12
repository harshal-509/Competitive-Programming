#Author: harshal_509
import sys
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=n
    b=n-1
    c=n-1
    arr=[]
    for i in range(n):
        arr.append(input())
    for i in range(c):
        arr.append(input())
    ans=""
    for i in range(m):
        k=0
        for j in range(a+b):
            h=arr[j]
            k=k^ord(h[i])
        ans+=chr(k)
    print(ans)
    sys.stdout.flush()