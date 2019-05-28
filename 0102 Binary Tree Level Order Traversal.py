# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

# Solution 1, recursion
class Solution:
    def dfs(self, node, level, res):
        if node is None:
            return
        if level >= len(res):
            res.append([])
        self.dfs(node.left, level + 1, res)
        res[level].append(node.val)
        self.dfs(node.right, level + 1, res)
        
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        self.dfs(root, 0, res)
        
        return res

# Solution 2, iteration 
class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        
        if root is None:
            return res
        
        q = [root]
        
        while q:
            res.append([p.val for p in q])
            q = [x for p in q for x in [p.left, p.right] if x]
        
        return res

# Solution 2.1, iteration using deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
            for x in [p.left, p.right]:
                if x:
                    q.append([x, h])
        
        return res