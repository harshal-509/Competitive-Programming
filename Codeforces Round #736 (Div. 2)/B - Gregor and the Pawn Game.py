#Author:harshal_509
import math
for _ in range(int(input())):
    n=int(input())
    l=list(input())
    m=list(input())
    ans=0
    for i in range(n-1):
        if(l[i]=="0" and m[i]=="1"):
            ans+=1
            continue
        if(i!=0):
            if(l[i-1]==m[i] and m[i]=="1"):
                ans+=1
                l[i-1]="-1"
            elif(l[i+1]==m[i] and m[i]=="1"):
                ans+=1
                l[i+1]="-1"
        else:
            if(l[i+1]==m[i] and m[i]=="1"):
                ans+=1
                l[i+1]="-1"
    if(l[-1]=="0" and m[-1]=="1"):
        ans+=1
    elif(l[-2]==m[-1] and m[-1]=="1"):
        ans+=1
        m[i-1]="-1"
    print(ans)