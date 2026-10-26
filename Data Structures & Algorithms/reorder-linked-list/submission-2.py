# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def split_list(head):
            slow = fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            second = slow.next
            slow.next = None
            return head, second
        
        def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        if not head:
            return
        elif not head.next:
            return
        else:
            first_half,second_half = split_list(head)
            second_half = reverse_list(second_half)

            l1, l2 = first_half, second_half

            while l2:
                n1 = l1.next
                n2 = l2.next

                l1.next = l2
                l2.next = n1

                l1 = n1
                l2 = n2    