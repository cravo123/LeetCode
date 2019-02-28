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
        path.append(node.val)
        if node.left is None and node.right is None:
            res.append(path[::])
            path.pop()
            return
        self.dfs(node.left, path, res)
        self.dfs(node.right, path, res)
        path.pop()
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        res = []
        path = []
        
        self.dfs(root, path, res)
        
        res = ['->'.join(str(x) for x in path) for path in res]
        
        return res