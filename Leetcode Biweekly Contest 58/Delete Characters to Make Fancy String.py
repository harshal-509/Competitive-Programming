#Author : koder_786
class Solution:
    def makeFancyString(self, s: str) -> str:
        n=len(s)
        ans=s[0]
        if(n<3):
            return s
        for i in range(1,n-1):
            if(s[i]==s[i-1] and s[i]==s[i+1]):
                pass
            else:
                ans+=s[i]
        return ans+s[n-1]