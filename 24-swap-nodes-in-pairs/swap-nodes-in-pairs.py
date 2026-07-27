# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        # elif head.next.next==None:
        #     temp=head
        #     temp=temp.next
        #     temp.next=head
        #     head.next=None
        #     return temp
        temp2=head
        temp2=temp2.next
        new_head=temp2.next
        temp2.next=head
        head.next=self.swapPairs(new_head)
        return temp2