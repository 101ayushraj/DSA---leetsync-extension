# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans=0
        tracker=0
        def solve(root,ans,tracker):
            if not root:
                return ans
            tracker+=1
            ans=max(ans,tracker)
            ans=solve(root.left,ans,tracker)
            ans=solve(root.right,ans,tracker)
            return ans
        
        return solve(root,ans,tracker)
        

           