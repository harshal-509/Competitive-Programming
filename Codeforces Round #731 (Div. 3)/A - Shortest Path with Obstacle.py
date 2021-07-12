#Author:harshal_509
for _ in range(int(input())):
    s=input()
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    e,f=map(int,input().split())
    ans=0
    j=min(b,d) ;
    k=min(a,c) ;
    l=max(b,d) ;
    m=max(a,c)
    if(a==c and b==d):
        print(0)
    elif(a==c and e==a and f>=j and f<=l):
        print(abs(c-a)+abs(d-b)+2)
    elif(b==d and f==b and e>=k and e<=m):
        print(abs(c-a)+abs(d-b)+2)
    else:
        print(abs(c-a)+abs(d-b))