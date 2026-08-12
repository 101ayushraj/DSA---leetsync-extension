# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=root
        if not root:
            return TreeNode(val)
        while node:
            if node.val<val:
                if not node.right:
                    break
                node=node.right
            else:
                if not node.left:
                    break
                node=node.left
        
        if node.val>val:
            node.left=TreeNode(val)
        else:
            node.right=TreeNode(val)
        
        return root