import collections

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

# Solution 2, Iteration using deque
class Codec:
    sep = ','
    null = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        res = []
        
        while q:
            t = []
            for p in q:
                if p is None:
                    res.append(self.null)
                else:
                    res.append(str(p.val))
                    t.append(p.left)
                    t.append(p.right)
            q = t
        
        res = self.sep.join(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q = data.split(self.sep)
        
        if not q or q[0] == self.null:
            return
        root = TreeNode(q[0])
        
        curr = collections.deque([root])
        
        i = 1
        while i < len(q):
            L, R = q[i], q[i + 1]
            p = curr.popleft()
            if L != self.null:
                p.left = TreeNode(int(L))
                curr.append(p.left)
            
            if R != self.null:
                p.right = TreeNode(int(R))
                curr.append(p.right)
            i += 2
        return root

# Solution 3, deque, elegant solution
class Codec:
    sep = ','
    null = '#'
    
    def dfs1(self, node, q):
        if node is None:
            q.append(self.null)
            return
        q.append(str(node.val))
        self.dfs1(node.left, q)
        self.dfs1(node.right, q)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = []
        self.dfs1(root, q)
        res = self.sep.join(q)
        return res
    
    def dfs2(self, q):
        v = q.popleft()
        if v == self.null:
            return
        root = TreeNode(v)
        root.left = self.dfs2(q)
        root.right = self.dfs2(q)
        
        return root
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
       
        q = collections.deque(data.split(self.sep))
        
        res = self.dfs2(q)
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))