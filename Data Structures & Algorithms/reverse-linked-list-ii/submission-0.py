# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        idx = 1
        root = head
        crt = root

        while idx < left:
            prev = crt
            crt = crt.next
            idx += 1

        while idx <= right:

            if idx==left:
                dummy = ListNode(crt.val)
                dummy_root = dummy
                
            else:
                node = ListNode(crt.val)
                node.next = dummy
                dummy = node
            
            crt = crt.next
            idx += 1
        
        if left>1:
            prev.next = dummy
        dummy_root.next = crt

        return root if left>1 else dummy





        