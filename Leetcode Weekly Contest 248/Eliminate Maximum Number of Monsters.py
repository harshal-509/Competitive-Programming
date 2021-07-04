#Author : koder_786
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        x=1
        l=zip(speed,dist)
        z=list(l)
        z=sorted(z,key=lambda i:i[1]/i[0])
        for i in range(1,len(z)):
            if(x*z[i][0]>=z[i][1]):
                return i
            x+=1
        return len(speed)