class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        length=len(stones)
        if length==1:
            return stones[0]
        target=int(sum(stones)//2)
        
        dp=[[False] * (target + 1) for _ in range(length+1)]

        dp[0][0]=True

        for i in range(1,length + 1):
            num=stones[i-1]
            for j in range(target+1):
                if num<=j:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-num]
                else:
                    dp[i][j]=dp[i-1][j]
        print(dp)
        for i,val in enumerate(dp[-1][::-1]):
            print(target+1-i,val , sum(stones))
            if val:
                return sum(stones) - 2*(target-i)

        return 0

