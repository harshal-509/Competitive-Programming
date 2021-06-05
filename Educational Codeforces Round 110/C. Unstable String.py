#Author : harshal_509
for i in range(int(input())):
    s=input()
    h=[-1]*2
    ans=0
    for i in range(len(s)):
        if(s[i]=="0" or s[i]=="1"):
            h[(i%2)^int(s[i])]=i
        q=min(h)
        ans+=i-q
    print(ans)