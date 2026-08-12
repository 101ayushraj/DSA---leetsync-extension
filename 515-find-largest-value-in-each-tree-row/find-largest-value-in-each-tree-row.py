# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        curr=deque([root])
        if not root:
            return []
        while curr:
            curr_max=min([s.val for s in curr])
            for _ in range(len(curr)):
                last=curr.popleft()
                curr_max=max(curr_max,last.val)
                if last.left:
                    curr.append(last.left)
                if last.right:
                    curr.append(last.right)
            
            ans.append(curr_max)

        return ans
                
                