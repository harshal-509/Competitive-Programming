#Author : harshal_509
import math
def primeFactors(n):
    count=0
    while n % 2 == 0:
        count+=1
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            count+=1
            n=n//i
    if(n>2):
        count+=1
    return count
for _ in range(int(input())):
    a,b,k=map(int,input().split())
    c=0
    if(k>60):
        print("No")
    else:
        if(a==b):
            p=2
        elif(a%b==0 or b%a==0):
            p=1
        else:
            p=2
        g=math.gcd(a,b)
        q=primeFactors(a//g)+primeFactors(b//g)+primeFactors(g)*2
        if(k>=p and k<=q):
            print("Yes")
        else:
            print("No")
