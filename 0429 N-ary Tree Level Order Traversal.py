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
    def dfs(self, node, level, res):
        if node is None:
            return
        if level >= len(res):
            res.append([])
        res[level].append(node.val)
        
        for p in node.children:
            self.dfs(p, level + 1, res)
        
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        res = []
        
        self.dfs(root, 0, res)
        
        return res


# Solution 2, iteration
class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        res = []
        
        if root is None:
            return res
        
        q = [root]
        
        while q:
            res.append([p.val for p in q])
            
            q = [x for p in q for x in p.children]
        
        return res

# Solution 2.1, iteration using deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        
        if root is None:
            return res
        
        q = collections.deque()
        q.append([root, 0])
        
        while q:
            p, h = q.popleft()
            if h == len(res):
                res.append([])
            res[h].append(p.val)
            
            h += 1
            for x in p.children:
                q.append([x, h])
        
        return res