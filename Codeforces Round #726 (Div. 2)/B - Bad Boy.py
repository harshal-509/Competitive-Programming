#Author: harshal_509
for _ in range(int(input())):
    n,m,i,j=map(int,input().split())
    if(not(i==1 and j==1) and not (i==n and j==m)):
        print(1,1,n,m)
    else:
        print(n,1,1,m)