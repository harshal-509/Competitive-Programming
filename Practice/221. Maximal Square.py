class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        ans=0
        m=len(matrix[0])
        dp=[[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            if(matrix[0][i]=="1"):
                dp[0][i]=1
                ans=1
        for i in range(n):
            if(matrix[i][0]=="1"):
                dp[i][0]=1
                ans=1
        for i in range(1,n):
            for j in range(1,m):
                if(matrix[i][j]=="1"):
                    dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                    ans=max(ans,dp[i][j])
        return ans**2
