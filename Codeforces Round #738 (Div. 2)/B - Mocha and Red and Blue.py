#Author:harshal_509
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    ans=""
    x=0
    i=0
    while(i<n and s[i]=="?"):
        x+=1
        i+=1
    flag=-1
    if(i<n and s[i]=="R"):
        flag=1
        if(x%2==0):
            ans+="RB"*(x//2)
        else:
            ans+=("BR"*(x//2))+"B"
    elif(i<n and s[i]=="B"):
        flag=0
        if(x%2==0):
            ans+="BR"*(x//2)
        else:
            ans+=("RB"*(x//2))+"R"
    if(flag==-1):
        if(x%2==0):
            ans+="RB"*(x//2)
        else:
            ans+="RB"*(x//2)+"R"
    while(i<n):
        if(s[i]=="?"):
            if(flag):
                ans+="B"
                flag=0
            else:
                ans+="R"
                flag=1
        elif(s[i]=="R"):
            flag=1
            ans+="R"
        elif(s[i]=="B"):
            flag=0
            ans+="B"
        i+=1
    print(ans)