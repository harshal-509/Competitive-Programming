#Author:harshal_509
import math
for _ in range(int(input())):
    n=int(input())
    s=input()
    ans=[["s" for i in range(n)] for j in range(n)]
    x=s.count("2")
    if(x==1 or x==2):
        print("NO")
    else:
        print("YES")
        for i in range(n):
            ans[i][i]="X"
        for i in range(n):
            if(s[i]=="2"):
                flag=1
                for k in range(n):
                    if(ans[i][k]!="+" and ans[i][k]!="-" and ans[i][k]!="=" and ans[i][k]!="X"):
                        if(flag and s[k]!="1"):
                            ans[i][k]="+"
                            ans[k][i]="-"
                            flag=0
                        else:
                            ans[i][k]="-"
                            ans[k][i]="+"
        for i in ans:
            print("".join(i))
