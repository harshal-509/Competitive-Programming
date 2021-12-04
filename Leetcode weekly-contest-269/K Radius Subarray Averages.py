class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        # Python program to find sum between two indexes
        # when there is no update.
        n=len(nums)
        # Function to compute prefix sum
        def preCompute(arr, n, prefix):
          prefix[0] = arr[0]
          for i in range(1, n):
            prefix[i] = prefix[i - 1] + arr[i]

        # Returns sum of elements in arr[i..j]
        # It is assumed that i <= j
        def rangeSum(l, r):
          if l == 0:
            return (prefix[r])
          return(prefix[r] - prefix[l - 1])
        prefix = [0 for i in range(n)]
        preCompute(nums, n, prefix)
        ans=[]
        if(k==0):
            return nums
        for i in range(n):
            if(i-k>=0 and i+k<n):
                ans.append(rangeSum(i-k,i+k)//(2*k+1))
            else:
                ans.append(-1)
        return ans