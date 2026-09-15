class Solution:
    def numSquares(self, n: int) -> int:
        if n==1:
            return 1
        def perfect(num):
            nums=[]
            for i in range(1,num):
                if i ** 2 <= num:
                    nums.append(i**2)
                else:
                    break
            return nums
        
        nums=perfect(n)
        print(nums)
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for num in nums:
            for i in range(n+1):
                if i>=num:
                    dp[i]=min(dp[i] , 1 + dp[i-num])
        return dp[-1]

