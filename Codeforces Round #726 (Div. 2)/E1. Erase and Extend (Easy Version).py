#Author: harshal_509
n,m=map(int,input().split())
s=input()
i=1
ans=s[0]*m
while(i<n):
    if(s[i]>s[0]):
        break
    i+=1
    t=s[:i]
    a=m//len(t)
    b=m%len(t)
    ans=min(ans,t*a+t[:b])
print(ans)