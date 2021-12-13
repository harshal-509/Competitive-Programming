class Solution:
    def maxPower(self, s: str) -> int:
        ans=1
        a=s[0]
        b=1
        n=len(s)
        for i in range(1,n):
            if(a==s[i]):
                b+=1
            else:
                b=1
                a=s[i]
            ans=max(ans,b)
        return ans
