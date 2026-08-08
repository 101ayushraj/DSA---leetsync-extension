# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetsum: int) -> bool:
        curr_sum=0
        if not root:
            return False
        def solve(node,curr_sum):
            if not node:
                return False

            curr_sum=curr_sum+node.val
            
            if not node.right and not node.left:
                return curr_sum==targetsum
            

            return solve(node.left,curr_sum) or solve(node.right,curr_sum)
        
        return solve(root,curr_sum)
                
