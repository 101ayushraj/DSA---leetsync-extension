class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        m=len(grid)

        if m==n==1:
            return grid[0][0]

        dp=[[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(1,n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for j in range(1,m):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=grid[i][j] + min(dp[i][j-1] , dp[i-1][j])
        
        return dp[-1][-1]