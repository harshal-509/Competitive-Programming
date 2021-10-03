#Author : koder_786
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s=sum(rolls)
        m=len(rolls)
        if((s+n)//(m+n)>mean or (s+6*n)//(m+n)<mean):
            return []
        else:
            t=mean*(n+m)-s
            k=t//n
            if(k<=0 or k>6):
                return []
            ans=[1 for i in range(n)]
            for i in range(n-1):
                ans[i]=k
                t-=k
            if(t>6):
                ans[n-1]=6
                t-=6
                for i in range(n-2,-1,-1):
                    x=min(t,6-ans[i])
                    t-=min(t,6-ans[i])
                    ans[i]+=x
                    if(t==0):
                        break
            else:
                ans[n-1]=t
            return ans