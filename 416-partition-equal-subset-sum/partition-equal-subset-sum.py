class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2==1:
            return False

        target=int(sum(nums)/2)
        
        dp=[True] + [False] * target

        for num in nums:
            for j in range(target,num-1,-1):
                dp[j]=dp[j] or dp[j-num]
        
        return dp[target]