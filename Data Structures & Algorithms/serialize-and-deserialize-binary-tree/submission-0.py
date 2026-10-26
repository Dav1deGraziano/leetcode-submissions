from collections import deque

class Codec:

    def serialize(self, root):

        if root is None:
            return ""

        out = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node is None:
                out.append("null")
            else:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        while out and out[-1] == "null":   
            out.pop()
        return ",".join(out)

    def deserialize(self, data):

        if not data:
            return None
            
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q and i < len(vals):
            node = q.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root