# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        queue = [root]
        k_smallest = []
        n_k_smallest = 0
        kth_min = -1

        while queue:

            node = queue.pop(0)

            if not node:
                continue
            
            queue.extend([node.left,node.right])

            if n_k_smallest<k:
                n_k_smallest += 1
                k_smallest.append(node.val)
                kth_min = max(kth_min,node.val)
                index_kth_min = k_smallest.index(kth_min)

            elif node.val < kth_min:
                k_smallest[index_kth_min] = node.val
                kth_min = max(k_smallest)
                index_kth_min = k_smallest.index(kth_min)
        
        return kth_min


