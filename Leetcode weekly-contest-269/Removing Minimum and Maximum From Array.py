class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        x=min(nums)
        y=max(nums)
        x=nums.index(x)
        y=nums.index(y)
        n=len(nums)
        x+=1
        y+=1
        return min(max(x,y),max(n-x+1,n-y+1),x+(n-y+1),y+(n-x+1))