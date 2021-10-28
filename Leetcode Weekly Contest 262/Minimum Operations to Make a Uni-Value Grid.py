class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr=[]
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j])
        arr.sort()
        n=len(arr)
        for i in range(1,n):
            if((arr[i]-arr[0])%x):
                return -1
        cost = 0
        k = arr[n//2]
        for i in range(n):
            cost = cost + abs(arr[i] - k)//x
        if n % 2 == 0:
            tempCost = 0
            K = arr[int(n / 2) - 1]
            for i in range(0, n):
                tempCost = tempCost + abs(arr[i] - k)//x
            cost = min(cost, tempCost)
        return cost