# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = head
        length = 1
        while dummy.next:
            length = length+1
            dummy = dummy.next

        if n == length:
            return head.next
        else:

            counter = 0
            dummy = head

            while counter<length-n:
                prev = dummy
                dummy = dummy.next
                counter = counter+1
            
            if n==1:
                prev.next = None
            else:
                prev.next = dummy.next
                
            return head
