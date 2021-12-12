class Solution:
    def countPoints(self, rings: str) -> int:
        rings.split()
        h=[set() for i in range(10)]
        n=len(rings)
        for i in range(1,n,2):
            h[int(rings[i])].add(rings[i-1])
        ans=0
        for i in h:
            if(len(i)>=3):
                ans+=1
        return ans