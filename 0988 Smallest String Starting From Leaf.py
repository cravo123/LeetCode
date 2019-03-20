# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, path, res):
        if node is None:
            return
        path.append(chr(ord('a') + node.val))
        if node.left is None and node.right is None:
            res.append(path[::])
            path.pop()
            return
        self.dfs(node.left, path, res)
        self.dfs(node.right, path, res)
        path.pop()
        
        
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        res = []
        path = []
        
        self.dfs(root, path, res)
        # No need to maintain the whole results though
        # We only need to save the current minimum string
        res = [''.join(path[::-1]) for path in res]
        res.sort()
        
        return res[0]