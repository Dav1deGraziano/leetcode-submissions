class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        vec = []
        counter = 0

        while head:
            vec.append(head.val)
            head = head.next
            counter += 1

        per_box = counter // k
        ans = [ListNode() for _ in range(k)]

        done = 0
        while k > 0:
            n = per_box + 1 if counter % k > 0 else per_box
            node = ans[-k]

            for i in range(n):
                node.next = ListNode(vec[done])
                node = node.next
                done += 1

            k -= 1
            counter -= n

        return [node.next for node in ans]