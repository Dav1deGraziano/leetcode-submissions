from typing import Optional

class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.length = 0
        self.capacity = capacity
        self.queue_LRU = None
        self.queue_MRU = None

    # FIXED: now properly modifies linked list
    def modify_queue(self, node: Node) -> None:
        if node is self.queue_MRU:
            return

        prev = node.prev
        nxt = node.next

        # detach node
        if prev:
            prev.next = nxt
        else:
            self.queue_LRU = nxt  # node was LRU

        if nxt:
            nxt.prev = prev

        # move to MRU (tail)
        node.prev = self.queue_MRU
        node.next = None

        if self.queue_MRU:
            self.queue_MRU.next = node

        self.queue_MRU = node

        if self.queue_LRU is None:
            self.queue_LRU = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, node = self.cache[key]
        self.modify_queue(node)
        return value

    def put(self, key: int, value: int) -> None:

        # update existing
        if key in self.cache:
            self.cache[key][0] = value
            self.modify_queue(self.cache[key][1])
            return

        node = Node(key)

        # empty case
        if self.length == 0:
            self.cache[key] = [value, node]
            self.queue_LRU = node
            self.queue_MRU = node
            self.length = 1
            return

        # eviction case
        if self.length == self.capacity:
            old_lru = self.queue_LRU
            del self.cache[old_lru.val]

            self.queue_LRU = old_lru.next
            if self.queue_LRU:
                self.queue_LRU.prev = None

            self.length -= 1

        # insert new node at MRU
        node.prev = self.queue_MRU
        if self.queue_MRU:
            self.queue_MRU.next = node

        self.queue_MRU = node

        if self.queue_LRU is None:
            self.queue_LRU = node

        self.cache[key] = [value, node]
        self.length += 1
        