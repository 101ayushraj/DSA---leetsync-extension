class Solution:
    def shipWithinDays(self, weights: List[int], max_days: int) -> int:
        left,right=max(weights),sum(weights)
        def solve(mid):
            days,added_sum=1,0
            for i in range(len(weights)):
                added_sum+=weights[i]
                if added_sum==0 and i != len(weights)-1:
                    days+=1
                    added_sum=0
                elif added_sum>mid:
                    days+=1
                    added_sum=weights[i]

            return days<=max_days
        while right>=left:
            mid=left+(right-left)//2
            if solve(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans

        