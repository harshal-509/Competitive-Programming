class Solution:
    def __init__(self):
        self.ans=0
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def subsetsUtil(A, subset, index,o):
            if(subset):
                x=subset[0]
                for i in range(1,len(subset)):
                    x=x|subset[i]
                if(x==o):
                    self.ans+=1
            for i in range(index, len(A)):
                subset.append(A[i])
                subsetsUtil(A, subset, i + 1,o)
                subset.pop(-1)
            
            return
        def subsets(A,o):
            subset = []
            index = 0
            subsetsUtil(A, subset, index,o)
        o=nums[0]
        for i in range(1,len(nums)):
            o=o|nums[i]
        subsets(nums,o)
        return self.ans