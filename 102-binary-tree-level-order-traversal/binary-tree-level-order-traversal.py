# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return ans

        curr=deque([root])
       
        while curr:
            curr_list=[]
            for _ in range(len(curr)):
                num=curr.popleft()

                curr_list.append(num)
                if num.left:
                    curr.append(num.left)
                if num.right:
                    curr.append(num.right)
            
            ans.append([s.val for s in curr_list])

        return ans
