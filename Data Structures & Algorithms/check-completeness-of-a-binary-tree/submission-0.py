from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root])
        seen_none = False

        while queue:

            node = queue.popleft()

            if node is None:
                seen_none = True
                
            else:
                if seen_none:          
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True