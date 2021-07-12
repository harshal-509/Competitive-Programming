#Author: harshal_509
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    o,e=[],[]
    for i in range(n):
        if(i%2==0):
            e.append(a[i])
        else:
            o.append(a[i])
    a.sort()
    o.sort()
    e.sort()
    p=0
    q=0
    flag=1
    for i in range(n):
        if(i%2==0):
            if(e[p]==a[i]):
                p+=1
                pass
            else:
                flag=0
                break
        else:
            if(o[q]==a[i]):
                q+=1
                pass
            else:
                flag=0
                break
    if(flag):
        print("YES")
    else:
        print("NO")