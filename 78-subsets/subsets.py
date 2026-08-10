class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        curr=[]
        def solve(index):

            if index == len(nums):
                ans.append(list(curr))
                return
            curr.append(nums[index])
            solve(index+1)
            curr.pop()
            solve(index+1)
            
        solve(0)
        return ans
