# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def tree_height(root: Optional[TreeNode]) -> int:

            if not root:
                return 0
            elif not root.left and not root.right:
                return 0
            else:
                return 1+max(tree_height(root.left),tree_height(root.right))
                
        
        if not root:
            return True
        elif not root.left and root.right:
            return tree_height(root.right)==0
        elif not root.right and root.left:
            return tree_height(root.left)==0
        else:
            if abs(tree_height(root.left)-tree_height(root.right))<=1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False

