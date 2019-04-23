import collections
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# Solution 1, similar idea as LC 0297 and LC 0449
# We need to memorize number of children for N-ary tree though

class Codec:
    sep = ','
    null = '#'
    
    def dfs1(self, node, q):
        if node is None:
            q.append(self.null)
            return
        q.append(str(node.val))
        q.append(str(len(node.children)))
        
        for p in node.children:
            self.dfs1(p, q)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        q = []
        self.dfs1(root, q)
        res = self.sep.join(q)
        return res
    
    def dfs2(self, q):
        if not q:
            return
        if q[0] == self.null:
            q.popleft()
            return
        root = Node(int(q[0]), [])
        cnt = int(q[1])
        for _ in range(cnt):
            q.popleft()
            q.popleft()
            root.children.append(self.dfs2(q))
        
        return root
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        q = collections.deque(data.split(self.sep))
        
        res = self.dfs2(q)
        
        return res

# Solution 2, same idea but we don't need to consider null node actually.
class Codec:
    sep = ','
    
    def dfs1(self, node, q):
        q.append(str(node.val))
        q.append(str(len(node.children)))
        
        for p in node.children:
            self.dfs1(p, q)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root is None:
            return ''
        q = []
        self.dfs1(root, q)    
        res = self.sep.join(q)
        return res
    
    def dfs2(self, q):
        v = q.popleft()
        cnt = q.popleft()
        
        root = Node(int(v), [])
        
        for _ in range(int(cnt)):
            root.children.append(self.dfs2(q))
        return root
        
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return
        q = collections.deque(data.split(self.sep))
        res = self.dfs2(q)
        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))