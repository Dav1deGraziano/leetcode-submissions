"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        copy = Node(head.val)
        res = copy
        created = [head]
        deep_copy_created = [copy]

        if head.random:
            if head.random not in created:
                copy.random = Node(head.random.val)
                created.append(head.random)
                deep_copy_created.append(copy.random)
            else:
                copy.random = copy

        while head.next:
            head = head.next
            if head not in created:
                copy.next = Node(head.val)
                copy = copy.next
                created.append(head)
                deep_copy_created.append(copy)
            else:
                copy.next = deep_copy_created[created.index(head)]
                copy = copy.next
            if head.random:
                if head.random not in created:
                    copy.random = Node(head.random.val)
                    created.append(head.random)
                    deep_copy_created.append(copy.random)
                else:
                    copy.random = deep_copy_created[created.index(head.random)]
        
        return res
                

            
