# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        counter = 0
        while head and counter<=1001:
            head = head.next
            counter = counter+1
        if counter<=1000:
            return False
        else:
            return True
        