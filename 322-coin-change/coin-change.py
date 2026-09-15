class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        length=len(coins)
        dp=[float('inf')] * (amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(amount+1):
                if i >=coin:
                    dp[i] = min(dp[i],1 + dp[i-coin])
        
        return -1 if dp[-1] == float('inf') else dp[-1]