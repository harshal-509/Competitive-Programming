#Author : koder_786
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        first_=0
        m=nums[first_]
        for i in range(1,len(nums)):
            if(nums[i]>=m):
                m=nums[i]
                first_=i
            else:
                break
        ans=[nums[first_]]
        if(first_==0):
            i=1
        else:
            i=first_
        flag=0
        while(first_<len(nums)-1 and i<len(nums)-1):
            if(flag==0):
                if(nums[i]>=nums[i+1]):
                    i+=1
                elif(nums[i]<nums[i+1] and i!=first_):
                    first_=i
                    ans.append(nums[i])
                    flag=1
            else:
                if(nums[i]<=nums[i+1]):
                    i+=1
                elif(nums[i]>nums[i+1] and i!=first_):
                    first_=i
                    ans.append(nums[i])
                    flag=0
        if(len(ans)%2==0):
            ans.append(nums[-1])
        ans1=0
        for i in range(len(ans)):
            if(i%2==0):
                ans1+=ans[i]
            else:
                ans1-=ans[i]
        return ans1
                