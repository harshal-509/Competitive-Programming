#Author:harshal_509
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    t=max(l)
    ans=0
    for i in range(1,n):
        ans=max(ans,l[i]*l[i-1])
    print(ans)