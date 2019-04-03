# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Codec:
    sep = ','
    
    def dfs1(self, node, path):
        if node is None:
            path.append('#')
            return
        path.append(str(node.val))
        self.dfs1(node.left, path)
        self.dfs1(node.right, path)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        path = []
        
        self.dfs1(root, path)
        res = self.sep.join(path)
        return res        

    def dfs2(self, path):
        if self.idx == len(path):
            return
        if path[self.idx] == '#':
            self.idx += 1
            return
        root = TreeNode(int(path[self.idx]))
        self.idx += 1
        root.left = self.dfs2(path)
        root.right = self.dfs2(path)
        
        return root
        
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        path = data.split(self.sep)
        self.idx = 0
        res = self.dfs2(path)
        
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))