# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
            
        res = ListNode()
        root = res
        n = len(lists)
        idx = None
        val = None
        for i in range(n):
            if lists[i]:
                if idx is None or lists[i].val<val:
                    idx,val = i,lists[i].val
        res.val = val
        lists[idx] = lists[idx].next

        ok = True
        while ok:
            ok = False
            idx,val = None,None
            for i in range(n):
                if lists[i]:
                    if idx is None or lists[i].val<val:
                        ok = True
                        idx,val = i,lists[i].val
            if ok:
                res.next = ListNode()
                res.next.val = val
                res = res.next
                lists[idx] = lists[idx].next
        
        return root
            

                    
        