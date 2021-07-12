#Author: harshal_509
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    dec,inc=0,0
    for i in range(n):
        if(a[i]<b[i]):
            dec+=b[i]-a[i]
        else:
            inc+=a[i]-b[i]
    if(dec!=inc):
        print("-1")
    else:
        ans=[]
        i=0
        j=len(a)-1
        while(i<len(a) and j>-1):
            if(a[i]>b[i] and a[j]<b[j]):
                while(a[i]!=b[i] and a[j]!=b[j]):
                    ans.append([i+1,j+1])
                    a[i]-=1
                    a[j]+=1
                if(a[i]==b[i]):
                    i+=1
                if(a[j]==b[j]):
                    j-=1
            else:
                if(a[i]<=b[i]):
                    i+=1
                if(a[j]>=b[j]):
                    j-=1
        print(len(ans))
        for i in (ans):
            print(*i)