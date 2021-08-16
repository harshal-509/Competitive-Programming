#Author:harshal_509
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=l[0]
    for i in range(1,n):
        ans=ans&l[i]
    print(ans)