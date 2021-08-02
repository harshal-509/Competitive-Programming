#Author : koder_786
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def sumNatural(n):
            sum = (n*(n+1))//2
            return sum
        def suminRange(l, r):
            return sumNatural(r) - sumNatural(l-1)
        ans=0
        i=0
        x=12
        j=2
        while(i<neededApples):
            i+=(x)
            t=j*2-1
            x=4*(3*j)+suminRange(j+1,2*j-1)*8
            j+=1
            ans+=1
        return ans*8