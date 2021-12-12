class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            x=nums[i]
            y=nums[i]
            for j in range(i+1,n):
                x=max(nums[j],x)
                y=min(nums[j],y)
                ans+=x-y
        return ans