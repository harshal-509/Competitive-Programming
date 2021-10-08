for _ in range(int(input())):
    l=list(input().split())
    n=int(l[0])
    c=l[1]
    s=input()
    a=0
    for i in range(n):
        if(s[i]!=c):
            a+=1
            k=i
    if(a==0):
        print(0)
    elif(a==1):
        if(k==n-1):
            print(1)
            print(k)
        else:
            print(1)
            print(k+2)
    else:
        flag=0
        for i in range(n-1,n//2-1,-1):
            if(s[i]==c):
                flag=i
                break
        if(flag):
            print(1)
            print(flag+1)
        else:
            print(2)
            print(n,n-1)