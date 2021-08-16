#Author : koder_786
mod=1000000007
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        x=pow(2,p)-1
        print(x)
        n=(x-1)
        ans=x
        ans=(pow(n,n//2,mod)*(x)%mod)%mod
        return ans