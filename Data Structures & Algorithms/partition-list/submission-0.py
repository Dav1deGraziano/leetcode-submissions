# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        head_l = l = ListNode()
        head_r = r = ListNode()

        while head:
            if head.val<x:
                l.next = ListNode(head.val)
                l = l.next
            else:
                r.next = ListNode(head.val)
                r = r.next
            head = head.next
        
        l.next = head_r.next

        return head_l.next
        