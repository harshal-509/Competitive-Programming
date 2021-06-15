#Author: harshal_509
def listToString(s): 
    str1 = ""
    return (str1.join(s))
for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        a=list(input())
        l.append(a)
    ans=[[-1 for i in range(m)] for i in range(n)]
    res=[[-1 for i in range(m)] for i in range(n)]
    k=0
    for i in range(n):
        for j in range(m):
            if((j+i)%2==0):
                res[i][j]="R"
            else:
                res[i][j]="W"
    for i in range(n):
        for j in range(m):
            if((j+i+1)%2==0):
                ans[i][j]="R"
            else:
                ans[i][j]="W"
    flag,falg=1,1
    for i in range(n):
        for j in range(m):
            if(l[i][j]=="."):
                pass
            else:
                if(l[i][j]!=res[i][j]):
                    falg=0
                    break
    for i in range(n):
        for j in range(m):
            if(l[i][j]=="."):
                pass
            else:
                if(l[i][j]!=ans[i][j]):
                    flag=0
                    break
    if(flag==0 and falg==0):
        print("NO")
    else:
        print("YES")
        if(falg):
            for i in res:
                print(listToString(i))
        else:
            for i in ans:
                print(listToString(i))
