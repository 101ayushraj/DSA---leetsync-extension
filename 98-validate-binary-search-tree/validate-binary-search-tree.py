# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        collection=[]
        def solve(node,low=float('-inf'),high=float('inf')):

            if not node:
                return True

            if not (low<node.val<high):
                return False
                    
            return solve(node.right,node.val,high) and solve(node.left,low,node.val)

        return solve(root) 
            
