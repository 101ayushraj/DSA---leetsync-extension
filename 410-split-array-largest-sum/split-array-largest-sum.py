class Solution:
    def splitArray(self, nums: List[int], k_max: int) -> int:
        
        left,right=max(nums),sum(nums)
        
        def solve(mid):
            results=[]
            k,added_sum=1,0,
            for i in range(len(nums)):
                added_sum+=nums[i]
                if added_sum>mid:
                    k+=1
                    added_sum=nums[i]
            return k <= k_max
            
        ans=right
        while right>=left:
            mid=left+(right-left)//2
            
            if solve(mid):
                ans=min(ans,mid)
                right=mid-1
            else:
                left=mid+1
        return ans