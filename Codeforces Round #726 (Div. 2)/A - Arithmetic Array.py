#Author: harshal_509
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    y=sum(l)
    if(y==n):
        print(0)
    elif(y<n):
        print(1)
    else:
        print(y-n)