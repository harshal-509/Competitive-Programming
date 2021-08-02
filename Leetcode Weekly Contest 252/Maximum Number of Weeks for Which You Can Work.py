#Author : koder_786
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones=sorted(milestones,reverse=True)
        ans=0
        n=len(milestones)
        if(n==1):
            return 1
        arr=[0 for i in range(n)]
        arr[-1]=milestones[-1]
        for i in range(n-2,-1,-1):
            arr[i]=arr[i+1]+milestones[i]
        for i in range(n-1):
            ans+=min(milestones[i],arr[i+1]+1)
        return min(milestones[0],arr[1]+1)+arr[1]