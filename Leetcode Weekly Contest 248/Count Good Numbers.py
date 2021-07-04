#Author : koder_786
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        x=int(1e9+7)
        if(n%2==0):
            return (((pow(4,n//2,x))%x)*(pow(5,n//2,x))%x)%x
        else:
            return (((pow(4,n//2,x))%x)*(pow(5,n//2+1,x))%x)%x