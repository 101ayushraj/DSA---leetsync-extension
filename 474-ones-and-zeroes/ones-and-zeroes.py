class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length=len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]
        def counter(a):
            zeros=0
            ones=0
            for i in a:
                if i == '0':
                    zeros += 1
                else:
                    ones += 1
            return zeros,ones
        
        for i in range(1,length+1):
            word=strs[i-1]
            zeros=counter(word)[0]
            ones=counter(word)[1]
            for k in range(m+1):
                for j in range(n+1):
                    if j >= ones and k>=zeros:
                        dp[i][k][j]=max(dp[i-1][k][j] , 1 + dp[i-1][k-zeros][j-ones])
                    else:
                        dp[i][k][j] = dp[i-1][k][j]

        return dp[length][m][n]