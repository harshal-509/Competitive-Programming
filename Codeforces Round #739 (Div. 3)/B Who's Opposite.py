for _ in range(int(input())):
    a,b,c=map(int,input().split())
    t=(abs(a-b))
    if(2*t<a or 2*t<b or 2*t<c):
        print(-1)
    else:
        print((c+t-1)%(2*t)+1)
