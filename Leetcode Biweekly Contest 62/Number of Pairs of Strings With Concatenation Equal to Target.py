#Author : koder_786
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n=len(nums)
        a=0
        for i in range(n):
            for j in range(n):
                if(i!=j and nums[i]+nums[j]==target):
                    a+=1
        return a