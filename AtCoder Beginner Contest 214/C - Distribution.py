#Author:koder_786
n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
k=float("inf")
temp=0
for i in range(n):
    if(m[i]<k):
        k=m[i]
        temp=i
ans=[m[temp]]
ctr=0
t=0
i=temp
while(ctr<n):
    ans.append(min(l[i]+ans[t],m[(i+1)%n]))
    ctr+=1
    t+=1
    i=(i+1)%n
ctr=0
i=n-temp
while(ctr<n):
    print(ans[i])
    ctr+=1
    i=(i+1)%n