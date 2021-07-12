#Author:harshal_509
def help(c,m,p,v,count,h):
    global ans
    if(c<0.000001):
        c=0
    if(m<0.000001):
        m=0
    if(c==0 and m==0):
        ans=ans+p*count*h
        return
    ans=ans+h*p*count
    x,y,z=c,m,p
    if(c!=0):
        if(m!=0):
            if(c<=v):
                m=m+c/2
                p=p+c/2
            else:
                m=m+v/2
                p=p+v/2
        else:
            if(c<=v):
                p=p+c
            else:
                p=p+v
        c=max(0.0,c-v)
        help(c,m,p,v,count+1,h*x)
    c,m,p=x,y,z
    if(m!=0):
        if(c!=0):
            if(m<=v):
                c=c+m/2
                p=p+m/2
            else:
                c=c+v/2
                p=p+v/2
        else:
            if(m<=v):
                p=p+m
            else:
                p=p+v
        m=max(0.0,m-v)
        help(c,m,p,v,count+1,h*y)
for _ in range(int(input())):
    c,m,p,v=map(float,input().split())
    ans=0
    help(c,m,p,v,1,1.0)
    print('%.25f'%ans)