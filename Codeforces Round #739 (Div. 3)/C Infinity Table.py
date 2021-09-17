x=1
t=2
arr=[]
while(x<1000000000):
    arr.append(x)
    x+=t
    t+=2
t=len(arr)
for _ in range(int(input())):
    n=int(input())
    i=0
    ans2,ans1=0,0
    for i in range(t):
        if(n>=arr[i]-i and n<=arr[i]+i):
            if(n>arr[i]):
                m=abs(n-arr[i]) 
                ans1=i+1
                ans2=i+1-m  
            elif(n<arr[i]):
                q=abs(n-arr[i]) 
                ans1=i+1-q 
                ans2=i+1
            else:
                ans1=i+1
                ans2=i+1
    print(ans1,ans2)