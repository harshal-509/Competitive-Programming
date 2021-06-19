#Author: harshal_509
import math
for _ in range(int(input())):
    n=int(input())
    if(n%2==1):
        print("Bob")
    else:
        if(n and not(n & (n-1))):
            if(int(math.log(n,2))%2==0):
                print("Alice")
            else:
                print("Bob")
        else:
            print("Alice")