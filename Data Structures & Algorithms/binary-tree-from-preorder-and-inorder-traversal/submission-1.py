# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        n = len(preorder)

        if n==0:
            return None

        root = TreeNode(preorder[0])

        if n==1:
            return root
        elif n==2:
            if preorder[0]!=inorder[0]:
                root.left = TreeNode(preorder[1])
            else:
                root.right = TreeNode(preorder[1])
            return root
        
        idx_left = inorder.index(preorder[0])
        if idx_left>=1 and idx_left<n-1:
            root.left = self.buildTree(preorder[1:idx_left+1],inorder[0:idx_left])
            root.right = self.buildTree(preorder[idx_left+1:],inorder[idx_left+1:])
        elif idx_left==n-1:
            root.left = self.buildTree(preorder[1:],inorder[0:-1])
        else:
            root.right = self.buildTree(preorder[1:],inorder[1:])
        
        return root
                