"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
import collections

# Solution 1, recursion
class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        if not node.children:
            return 1
        return 1 + max(self.dfs(p) for p in node.children)
        
    def maxDepth(self, root: 'Node') -> 'int':
        return self.dfs(root)

# Solution 1.1, more elegant implementation
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(p) for p in root.children + [None])

# Solution 2, iteration, level traversal
class Solution:
    def maxDepth(self, root: 'Node') -> 'int':
        levels = 0
        if root is None:
            return levels
        q = [root]
        
        while q:
            levels += 1
            q = [x for p in q for x in p.children if x]
        
        return levels

# Solution 2.1, another level traversal using deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        res = 0
        
        q = collections.deque()
        q.append([root, 1])
        
        while q:
            p, h = q.popleft()
            res = max(res, h)
            h += 1
            
            for child in p.children:
                q.append([child, h])
        
        return res