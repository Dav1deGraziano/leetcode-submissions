# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def IsDescendant(root: Optional[TreeNode],val: int) -> bool:
            if not root:
                return False
            else:
                if root.val==val:
                    return True
                else:
                    return IsDescendant(root.left,val) or IsDescendant(root.right,val)
        
        if p==q:
            return True
        else:
            current_node = root
            condition = True
            while condition:
                if p.val==current_node.val or q.val==current_node.val:
                    return current_node
                else:
                    if IsDescendant(current_node.left,p.val) and IsDescendant(current_node.left,q.val):
                        current_node = current_node.left
                    elif IsDescendant(current_node.right,p.val) and IsDescendant(current_node.right,q.val):
                        current_node = current_node.right
                    else:
                        condition = False
            return current_node

