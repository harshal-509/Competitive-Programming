#Author:koder_786
import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    if(math.gcd(x,y)>1):
        print(0)
    elif(math.gcd(x+1,y)>1 or math.gcd(x,y+1)>1):
        print(1)
    else:
        print(2)