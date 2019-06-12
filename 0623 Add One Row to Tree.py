# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        dummy = TreeNode(None)
        dummy.left = root
        
        q = [dummy]
        level = 1
        
        while level < d:
            q = [x for p in q for x in [p.left, p.right] if x]
            level += 1
        
        for p in q:
            tmp = TreeNode(v)
            tmp.left = p.left
            p.left = tmp

            tmp = TreeNode(v)
            tmp.right = p.right
            p.right = tmp
        
        return dummy.left

# DFS
class Solution:
    def dfs(self, node, curr, target, v):
        if node is None:
            return
        if curr == target - 1:
            p = TreeNode(v)
            p.left = node.left
            node.left = p
            
            p = TreeNode(v)
            p.right = node.right
            node.right = p
        else:
            self.dfs(node.left, curr + 1, target, v)
            self.dfs(node.right, curr + 1, target, v)
        
        
    def addOneRow(self, root: 'TreeNode', v: 'int', d: 'int') -> 'TreeNode':
        if d == 1:
            p = TreeNode(v)
            p.left = root
            return p
        
        self.dfs(root, 1, d, v)
        
        return root