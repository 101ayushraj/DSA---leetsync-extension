class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        m=len(obs)
        n=len(obs[0])
        
        if obs[0][0]==1:
            return 0
        if m==n==1:
            return 1

        dp=[[0] * n for _ in range(m)]

        for i in range(n):
            if obs[0][i]==1:
                break
            else:
                dp[0][i]=1
        for j in range(m):
            if obs[j][0]==1:
                break
            else:
                dp[j][0]=1

        dp[0][0]=0

        for i in range(1,m):
            for j in range(1,n):
                if obs[i][j]==1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]