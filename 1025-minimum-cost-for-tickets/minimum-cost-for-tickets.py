class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day=max(days)

        dp=[0] * ( max_day + 1 )

        for i in range(1,max_day+1):
            if i not in days:
                dp[i]=dp[i-1]
            else:
                buy_1_day=dp[max(0,i-1)] + costs[0]
                buy_7_day=dp[max(0,i-7)] + costs[1]
                buy_30_day=dp[max(0,i-30)] + costs[2]

                dp[i]=min(buy_1_day,buy_7_day,buy_30_day)

        return dp[max_day]