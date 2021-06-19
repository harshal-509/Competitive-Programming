#Author: harshal_509
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    a,b=l[0],l[1]
    m=abs(a-b)
    for i in range(1,n):
        if(abs(l[i-1]-l[i])<=m):
            m=abs(l[i-1]-l[i])
            a=i
    ans=l[a:]+l[:a]
    if(n==2):
        print(*ans[::-1])
    else:
        print(*ans)