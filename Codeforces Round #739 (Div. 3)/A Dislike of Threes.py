for _ in range(int(input())):
    n=int(input())
    arr=[]
    i=0
    x=0
    while(i<=1000):
        x+=1
        t=str(x)
        if(x%3!=0 and t[-1]!="3"):
            arr.append(x)
            i+=1
    print(arr[n-1])