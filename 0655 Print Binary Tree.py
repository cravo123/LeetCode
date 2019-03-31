# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth(self, node):
        if node is None:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
    
    def dfs(self, node, level, left, right, res):
        if node is None:
            return
        
        mid = (left + right) // 2
        res[level][mid] = str(node.val)
        
        level += 1
        self.dfs(node.left, level, left, mid - 1, res)
        self.dfs(node.right, level, mid + 1, right, res)
    
    def printTree(self, root: TreeNode) -> List[List[str]]:
        m = self.depth(root)
        n = int(2 ** m) - 1
        
        res = [['' for _ in range(n)] for _ in range(m)]
        
        level = 0
        self.dfs(root, level, 0, n - 1, res)
        
        return res
        
        