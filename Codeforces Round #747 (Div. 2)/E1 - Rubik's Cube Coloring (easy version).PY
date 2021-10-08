for _ in range(1):
    n=int(input())
    x=pow(2,n)-1
    ans=6
    mod=1000000007
    ans=((ans%mod)*pow(4,x-1,mod))%mod
    print(ans)