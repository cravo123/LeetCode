# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node, size, level, res):
        if node is None:
            return
        
        if level >= len(res):
            res.append([])
        
        self.dfs(node.left, size * 2, level + 1, res)
        res[level].append(size)
        self.dfs(node.right, size * 2 + 1, level + 1, res)
        
        
        
    def widthOfBinaryTree(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0
        res = []
        level = 0
        size = 1
        
        self.dfs(root, size, level, res)
        
        res = [row[-1] - row[0] + 1 for row in res]
        return max(res)

# Iteration
class Solution:
    def widthOfBinaryTree(self, root: 'TreeNode') -> 'int':
        res = 0
        if root is None:
            return res
        q = [[root, 1]]
        
        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)
            tmp = []
            for p, size in q:
                if p.left:
                    tmp.append([p.left, size * 2])
                if p.right:
                    tmp.append([p.right, size * 2 + 1])
            q = tmp
        
        return res
