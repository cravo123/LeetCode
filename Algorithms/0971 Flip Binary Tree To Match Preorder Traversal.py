# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, voyage, res):
        if node is None:
            return True
        
        if node.val != voyage[self.idx]:
            return False
        
        self.idx += 1
        if node.left is None:
            return self.dfs(node.right, voyage, res)
        
        L = node.left.val
        if L == voyage[self.idx]:
            return self.dfs(node.left, voyage, res) and self.dfs(node.right, voyage, res)
        else:
            res.append(node.val)
            return self.dfs(node.right, voyage, res) and self.dfs(node.left, voyage, res)
        
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        self.idx = 0
        
        if not self.dfs(root, voyage, res):
            return [-1]
        
        return res