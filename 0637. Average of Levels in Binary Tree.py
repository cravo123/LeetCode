# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Same idea as plain level traversal of binary tree, we just need
# to post-process res to get level average values

# Recursion
class Solution:
    def dfs(self, node, level, res):
        if node is None:
            return
        if level >= len(res):
            res.append([])
        res[level].append(node.val)
        
        level += 1
        self.dfs(node.left, level, res)
        self.dfs(node.right, level, res)
        
    def averageOfLevels(self, root: 'TreeNode') -> 'List[float]':
        res = []
        
        self.dfs(root, 0, res)
        
        res = [sum(row) / len(row) for row in res]
        
        return res


# Iteration
class Solution:
    def averageOfLevels(self, root: 'TreeNode') -> 'List[float]':
        res = []
        if root is None:
            return res
        
        q = [root]
        
        while q:
            tmp = [p.val for p in q]
            res.append(sum(tmp) / len(tmp))
            
            q = [x for p in q for x in [p.left, p.right] if x]
        
        return res
