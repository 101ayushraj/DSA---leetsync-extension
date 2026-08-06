# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return None
        if original is target:
            return cloned
        left_res=self.getTargetCopy(original.left,cloned.left,target)
        
        if left_res:
            return left_res

        return self.getTargetCopy(original.right,cloned.right,target)