class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_num=max(nums)
        if max_num == 1:
            return nums.count(1)
        
        tracker = {i: 0 for i in range(1, max(nums) + 1)}
        for num in nums:
            tracker[num] += 1

        dp = [0] * (max_num + 1)
        dp[1] = tracker.get(1, 0) * 1
        dp[2] = max(dp[1], tracker.get(2, 0) * 2)

        for i in range(3, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + tracker.get(i, 0) * i)

        return dp[-1]