#Author : koder_786
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        k=0
        a=nums
        for j in range(1,len(a)):
            if(a[j]>a[j-1]):
                k+=1
        if(k==len(a)-1):
            return True
        for i in range(len(nums)):
            a=nums[:i]+nums[i+1:]
            t=0
            for j in range(1,len(a)):
                if(a[j]>a[j-1]):
                    t+=1
            if(t==len(a)-1):
                return True
        return False