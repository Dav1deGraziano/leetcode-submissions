# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = l1
        res = ListNode(0)
        number = res

        while l1 or l2:
            add = 0
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            add += number.val
            if add<=9:
                number.val = add
                if l1 or l2:
                    number.next = ListNode(0)
                    number = number.next
            else:
                add = str(add)
                number.val = int(add[1])
                number.next = ListNode(int(add[0]))
                number = number.next

        return res