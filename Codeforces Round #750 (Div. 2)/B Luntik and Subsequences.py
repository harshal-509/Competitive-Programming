from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=l.count(1)
    if(not(x)):
        print(0)
    else:
        ans=1
        for i in range(n):
            if(l[i]==0):
                ans*=2
        print(ans*x)