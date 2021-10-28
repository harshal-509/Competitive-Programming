for i in range(int(input())):
    a,b,c=map(int,input().split())
    a=a%2
    b=b%2
    c=c%2
    if(c):
        print(c*3-2*b-a*1)
    else:
        print(2*b-a*1)