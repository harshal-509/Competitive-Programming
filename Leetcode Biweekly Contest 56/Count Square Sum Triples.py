#Author : koder_786
class Solution:
    def countTriples(self, n: int) -> int:
        a=0
        for i in range(1,n):
            for j in range (i,n):
                if(math.sqrt(pow(i,2)+pow(j,2))<=n and math.sqrt(pow(i,2)+pow(j,2))== int(math.sqrt(pow(i,2)+pow(j,2)))):
                    a+=2
        return a