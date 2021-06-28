#Author:harshal_509
for _ in range(int(input())):
    n=int(input())
    m=dict()
    l=list(map(int,input().split()))
    ans=0
    for i in range(1,n+1):
        m[l[i-1]]=i
    for i in range(1,2*n+1):
        j=1
        while(j*j<=i):
            if(i%j==0):
                if(j!=i//j):
                    if(j in m and (i//j) in m):
                        if(i==m[j]+m[i//j]):
                            ans+=1
            j+=1
    print(ans)