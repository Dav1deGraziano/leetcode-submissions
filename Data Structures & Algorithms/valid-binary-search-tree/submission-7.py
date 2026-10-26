class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        queue = [(root, None, None)]

        while queue:
            node, low, high = queue.pop(0)

            if not node:
                continue

            # violate low bound
            if low is not None and node.val <= low:
                return False

            # violate high bound
            if high is not None and node.val >= high:
                return False

            queue.append((node.left, low, node.val))
            queue.append((node.right, node.val, high))

        return True