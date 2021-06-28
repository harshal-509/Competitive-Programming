#Author:harshal_509
for _ in range(int(input())):
    n=int(input())
    if(n%2==0):
        ans=[]
        for i in range(2,n+1,2):
            ans.append(i)
            ans.append(i-1)
    else:
        ans=[]
        for i in range(2,n,2):
            ans.append(i)
            ans.append(i-1)
        ans.insert(n-2,n)
    print(*ans)