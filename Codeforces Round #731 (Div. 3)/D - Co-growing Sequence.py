#Author:harshal_509
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=[0]
    for i in range(1,n):
        h=bin(l[i])
        h=h[2:]
        x=bin(l[i-1])
        x=x[2:]
        t=max(len(h),len(x))
        x=(abs(len(x)-t))*"0"+x
        h=(abs(len(h)-t))*"0"+h
        q=""
        #print(h,x)
        for j in range(len(x)-1,-1,-1):
            if(x[j]=="1"):
                if(h[j]=="1"):
                    q+="0"
                else:
                    q+="1"
            else:
                q+="0"
        l[i]=int(q[::-1],2)^l[i]
        ans.append(int(q[::-1],2))
    print(*ans)