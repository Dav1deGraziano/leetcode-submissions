# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]
        
        result = [root.val]
        queue = [root]
        levels = [1]

        while queue:

            current_node = queue[0]
            current_level = levels[0]

            if not current_node.left and not current_node.right:
                queue = queue[1:]
                levels = levels[1:]
            else:
                if current_node.right:
                    if len(result)-levels[0]==0:
                        result.append(current_node.right.val)
                    queue[0] = current_node.right
                    levels[0] = levels[0]+1
                    if current_node.left:
                        queue = [queue[0]]+[current_node.left]+queue[1:]
                        levels = [levels[0]]+[levels[0]]+levels[1:]
                else:
                    if len(result)-levels[0]==0:
                        result.append(current_node.left.val)
                    queue[0] = current_node.left
                    levels[0] = levels[0]+1
                    
        return result



            