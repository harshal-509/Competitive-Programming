#Author:harshal_509
for _ in range(int(input())):
    n=int(input())
    q=[]
    for i in range(n):
        l=list(map(int,input().split()))
        q.append(l)
    ans=0
    i=1
    while(i<n):
        u,v,w,x,y=q[i][0]-q[ans][0],q[i][1]-q[ans][1],q[i][2]-q[ans][2],q[i][3]-q[ans][3],q[i][4]-q[ans][4]
        s=sorted([u,v,w,x,y])
        if(s[0]<0 and s[1]<0 and s[2]<0):
            ans=i
        i+=1
    flag=0
    count=0
    for i in range(n):
        u,v,w,x,y=q[i][0]-q[ans][0],q[i][1]-q[ans][1],q[i][2]-q[ans][2],q[i][3]-q[ans][3],q[i][4]-q[ans][4]
        s=sorted([u,v,w,x,y])
        if(s[2]>0 and s[3]>0 and s[4]>0):
            count+=1
    if(count==n-1):
        print(ans+1)
    else:
        print("-1")