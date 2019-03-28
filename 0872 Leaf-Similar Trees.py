# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion. In-order traversal, and add leaf node to res
class Solution:
    def dfs(self, node, res):
        if node is None:
            return
        if node.left is None and node.right is None:
            res.append(node.val)
            return
        
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res_1, res_2 = [], []
        
        self.dfs(root1, res_1)
        self.dfs(root2, res_2)
        
        return res_1 == res_2

# Solution 2, iteration
class Solution:
    def bfs(self, node):
        res = []
        if node is None:
            return res
        p, q = node, []
        
        while p or q:
            if p:
                q.append(p)
                p = p.left
            else:
                p = q.pop()
                if p.left is None and p.right is None:
                    res.append(p.val)
                p = p.right
        return res
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res_1, res_2 = self.bfs(root1), self.bfs(root2)
        
        return res_1 == res_2