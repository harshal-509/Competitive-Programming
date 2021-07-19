#Author : koder_786
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        n=len(rungs)
        ans=0
        if(rungs[0]>dist):
            if(rungs[0]%dist==0):
                ans+=rungs[0]//dist-1
            else:
                ans+=rungs[0]//dist
        for i in range(1,n):
            if(rungs[i]-rungs[i-1]<=dist):
                pass
            else:
                if(abs(rungs[i]-rungs[i-1])%dist==0):
                    ans+=abs(rungs[i]-rungs[i-1])//dist-1
                else:
                    ans+=abs(rungs[i]-rungs[i-1])//dist
        return ans