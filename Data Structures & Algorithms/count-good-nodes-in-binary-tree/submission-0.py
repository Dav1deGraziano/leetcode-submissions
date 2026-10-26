# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        counter = 1
        queue = []
        if root.left:
            if root.left.val >= root.val:
                counter += 1
            else:
                root.left.val = root.val
            queue.append(root.left)
        if root.right:
            if root.right.val >= root.val:
                counter += 1
            else:
                root.right.val = root.val
            queue.append(root.right)

        while queue:
            prev = queue
            queue = []
            for node in prev:
                if node.left:
                    if node.left.val >= node.val:
                        counter += 1
                    else:
                        node.left.val = node.val
                    queue.append(node.left)
                if node.right:
                    if node.right.val >= node.val:
                        counter += 1
                    else:
                        node.right.val = node.val
                    queue.append(node.right)

        
        return counter

        