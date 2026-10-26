# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def tree_length(root: Optional[TreeNode]) -> int:

            if not root:
                return 0
            else:
                if not root.left and not root.right:
                    return 0
                else:
                    return 1+max(tree_length(root.left),tree_length(root.right))
        
        if not root:
            return 0
        else:
            if not root.left and not root.right:
                return 0
            else:
                if not root.left and root.right:
                    return max(1+tree_length(root.right),self.diameterOfBinaryTree(root.right))
                elif not root.right and root.left:
                    return max(1+tree_length(root.left),self.diameterOfBinaryTree(root.left))
                else:
                    return max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right),2+tree_length(root.left)+tree_length(root.right))

        