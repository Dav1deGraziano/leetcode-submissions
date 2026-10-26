# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        if not root:
            return root

        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right,target)
        
        
        if root.left and root.left.val == target and not (root.left.left or root.left.right):
            root.left = None
        
        if root.right and root.right.val == target and not (root.right.left or root.right.right):
            root.right = None

        if not root.left and not root.right and root.val == target:
            return None
        
        return root
        
        