from collections import Counter
for _ in range(int(input())):
    n,k=map(int,input().split())
    t=bin(k)[2:]
    mod=1000000007
    a=0
    for i in range(len(t)-1,-1,-1):
        if(t[i]=="1"):
            a+=(pow(n,len(t)-i-1,mod))%mod
            a=a%mod
    print(a)