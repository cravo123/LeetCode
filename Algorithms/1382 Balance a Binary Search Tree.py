# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: DFS
class Solution:
    def dfs(self, node, q):
        if node is None:
            return 
        self.dfs(node.left, q)
        q.append(node.val)
        self.dfs(node.right, q)
    
    def build(self, q):
        if not q:
            return
        
        mid = len(q) // 2
        
        res = TreeNode(q[mid])
        res.left = self.build(q[0:mid])
        res.right = self.build(q[(mid + 1):])
        
        return res
        
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        q = []
        
        self.dfs(root, q)
        
        # build
        
        return self.build(q)