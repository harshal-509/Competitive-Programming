#Author: harshal_509
for _ in range(int(input())):
    n,m=map(int,input().split())
    ans=[]
    for i in range(n):
        ans.append("0"*m)
    s=""
    for i in range(m):
        if(i%2==0):
            s+="1"
        else:
            s+="0"
    ans[0]=s
    for i in range(1,n):
        if(i==1):
            if(ans[i-1][m-2]=="0" and ans[i-1][m-1]=="0"):
                s=ans[i][:len(ans[i])-1]
                ans[i]=s+"1"
        else:
            if(ans[i-1][m-1]=="0"):
                s=ans[i][:len(ans[i])-1]
                ans[i]=s+"1"
    for i in range(m-2,-1,-1):
        if(i==m-2):
            if(ans[n-2][i+1]=="0" and ans[n-1][i+1]=="0"):
                s=ans[n-1][:i]
                t=ans[n-1][i+1:]
                ans[n-1]=s+"1"+t
        else:
            if(ans[n-1][i+1]=="0"):
                s=ans[n-1][:i]
                t=ans[n-1][i+1:]
                ans[n-1]=s+"1"+t
    for i in range(n-2,0,-1):
        if(i==n-2):
            if(ans[i+1][1]=="0" and ans[i+1][0]=="0"):
                s=ans[i][1:]
                ans[i]="1"+s
        else:
            if(ans[i+1][0]=="0" and ans[i-1][0]=="0"):
                s=ans[i][1:]
                ans[i]="1"+s
    for i in ans:
        print(i)