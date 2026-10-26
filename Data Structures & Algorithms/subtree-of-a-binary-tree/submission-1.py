# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def IsSameTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

            if not root and not subRoot:
                return True
            elif not root and subRoot:
                return False
            elif root and not subRoot:
                return False
            else:
                if root.val!=subRoot.val:
                    return False
                else:
                    return IsSameTree(root.left,subRoot.left) and IsSameTree(root.right,subRoot.right)
        
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        elif root and not subRoot:
            return False
        else:
            if IsSameTree(root,subRoot):
                return True
            else:
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)