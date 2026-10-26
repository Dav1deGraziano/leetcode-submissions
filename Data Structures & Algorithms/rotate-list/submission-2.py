# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head
        
        n = 1
        root = head
        while root.next:
            n+=1
            root = root.next
        
        k = k%n

        if k == 0:
            return head
        
        k = n-k
        counter = 0
        root = head

        while counter < k:
            prev = root
            root = root.next
            counter += 1
        
        prev.next = None
        crt = root
        
        while crt and crt.next:
            crt = crt.next
        
        crt.next = head

        return root



        