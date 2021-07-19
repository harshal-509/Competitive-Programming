#Author:harshal_509
for _ in range(int(input())):
    space=input()
    n,k=map(int,input().split())
    arr=[0 for i in range(n)]
    arr1=[0 for i in range(n)]
    a=list(map(int,input().split()))    
    b=list(map(int,input().split()))
    for i in range(k):
        arr[a[i]-1]=b[i]
        arr1[a[i]-1]=b[i]
    val=-1
    co=-1
    for i in range(n):
        if(val==-1 and arr1[i]!=0):
            val=arr1[i]
            co=i
        elif(arr1[i]!=0):
            if(val+abs(co-i)>arr[i]):
                co=i
                val=arr[i]
        if(val!=-1):
            arr[i]=max(0,val+abs(co-i))
    val=-1
    co=-1
    for i in range(n-1,-1,-1):
        if(val==-1 and arr1[i]!=0):
            val=arr1[i]
            co=i
        elif(arr1[i]!=0):
            if(val+abs(co-i)>arr[i]):
                co=i
                val=arr[i]
        if(val!=-1):
            if(arr[i]==0):
                arr[i]=val+abs(co-i)
            else:
                arr[i]=min(arr[i],val+abs(co-i))
    print(*arr)