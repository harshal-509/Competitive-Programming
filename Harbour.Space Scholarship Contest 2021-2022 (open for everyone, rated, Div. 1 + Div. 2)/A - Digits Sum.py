#Author:harshal_509
import math
for _ in range(int(input())):
    n=int(input())
    if(n%10==9):
        print(n//10+1)
    else:
        print(n//10)