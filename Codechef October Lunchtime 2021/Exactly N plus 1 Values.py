# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n=int(input())
    ans=[]
    for i in range(n):
        ans.append(i+1)
    x=sum(ans)
    y=pow(2,n)
    ans.append(y-x)
    if(ans[-1]%2==0):
        if(ans[-2]%2==0):
            i=-2
        else:
            i=-3
    else:
        if(ans[-2]%2!=0):
            i=-2
        else:
            i=-3
    j=-1
    m=(ans[i]+ans[j])//2
    ans[i]=ans[i]+(m-ans[i])
    ans[j]=ans[j]-(ans[j]-m)
    print(*sorted(ans))