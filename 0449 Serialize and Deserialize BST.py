import bisect
import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Preorder of BST naturally define a unique BST

# Solution 1, recursion
# dfs2 can be improved to be O(n) by using lower and upper bound of series
class Codec:
    def dfs1(self, node, q):
        if node is None:
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
        
        if not q:
            return ''
        res = ','.join(q)
        
        return res
    
    def dfs2(self, start, end, q):
        if start > end:
            return
        if start == end:
            return TreeNode(q[start])
        
        root = TreeNode(q[start])
        
        idx = bisect.bisect_left(q, q[start], lo=start + 1)
        root.left = self.dfs2(start + 1, idx - 1, q)
        root.right = self.dfs2(idx, end, q)
        
        return root
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        q = data.split(',')
        q = [int(x) for x in q]
        
        res = self.dfs2(0, len(q) - 1, q)
        
        return res

# Solution 2, iterative and O(n) for deserialize
class Codec:
    def bfs1(self, root):
        if not root:
            return ''
        q = [root]
        res = []
        
        while q:
            p = q.pop()
            res.append(str(p.val))
            
            if p.right:
                q.append(p.right)
            if p.left:
                q.append(p.left)
        
        res = ','.join(res)
        return res    
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.bfs1(root)
    
    def dfs(self, low, up, data):
        if not data:
            return
        
        v = int(data[0])
        if v < low or v > up:
            return
        
        root = TreeNode(v)
        data.popleft()
        root.left = self.dfs(low, v, data)
        root.right = self.dfs(v, up , data)
        
        return root
        
    def bfs2(self, data):
        if not data:
            return
        data = collections.deque(data.split(','))
        
        return self.dfs(float('-inf'), float('inf'), data)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = self.bfs2(data)
        
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
