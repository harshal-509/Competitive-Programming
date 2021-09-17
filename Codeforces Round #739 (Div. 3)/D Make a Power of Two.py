arr=[]
for i in range(101):
    arr.append(pow(2,i))    
    ans=0
    t=len(arr)
for _ in range(int(input())):
    n=int(input())
    ans=10000000000000000
    for i in range(t):
        x=str(arr[i])
        y=str(n)
        j=0
        count=0
        k=0
        while(j<len(x) and k<len(y)):
            if(x[j]==y[k]):
                j+=1
                count+=1
            k+=1
        l=(len(y)-count)+(len(x)-count)
        ans=min(l,ans)
    print(ans)