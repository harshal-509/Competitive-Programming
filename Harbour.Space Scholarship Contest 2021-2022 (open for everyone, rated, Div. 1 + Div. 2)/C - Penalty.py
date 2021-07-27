#Author:harshal_509 
for _ in range(int(input())):
    z=input()
    ans=11
    t=[]
    for i in range(10):
        if(z[i]=="?"):
            if(i%2==0):
                t.append("1")
            else:
                t.append("0")
        else:
            t.append(z[i])
    d="".join(t)
    p,q,r,s=0,0,0,0
    k=0
    for i in range(10):
        if(d[i]=='1'):
            if(i%2==0):
                p+=1
            else:
                q+=1
        else:
            if(i%2==0):
                r+=1
            else:
                s+=1
        if p>5-s or q>5-+r:
            k=1
            break
    if k:
        ans=min(ans,i+1)
    else:
        ans=min(ans,10)
    t=[]
    for i in range(10):
        if(z[i]=="?"):
            if(i%2==0):
                t.append("0")
            else:
                t.append("1")
        else:
            t.append(z[i])
    d="".join(t)
    p,q,r,s=0,0,0,0
    k=0
    for i in range(10):
        if(d[i]=='1'):
            if(i%2==0):
                p+=1
            else:
                q+=1
        else:
            if(i%2==0):
                r+=1
            else:
                s+=1
        if p>5-s or q>5-+r:
            k=1
            break
    if k:
        ans=min(ans,i+1)
    else:
        ans=min(ans,10)        
    print(ans)