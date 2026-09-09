class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums) + target )%2 == 1 or abs(target) > sum(nums):
            return 0

        new_target = int( (sum(nums) + target ) / 2 )

        dp=[[0] * (new_target + 1) for _ in range(len(nums) + 1)]

        dp[0][0]=1

        for i in range(1,len(nums)+1):
            for j in range(new_target+1):
                if nums[i-1] <=  j :
                    dp[i][j]=dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]

        print(dp)
        return dp[-1][-1]