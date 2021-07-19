#Author: harshal_509
for _ in range(int(input())):
    n=int(input())
    s=0
    a=0
    l=1
    while(s<n):
        s+=l
        l+=2
        a+=1
    print(a)