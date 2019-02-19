# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node, target):
        if node is None:
            return True
        if node.val != target:
            return False
        return self.dfs(node.left, target) and self.dfs(node.right, target)
        
    def isUnivalTree(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True
        
        return self.dfs(root, root.val)

# Iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True
        
        seen = set()
        q = [root]
        
        while q:
            p = q.pop()
            seen.add(p.val)
            if len(seen) > 1:
                return False
            for x in [p.right, p.left]:
                if x:
                    q.append(x)
        return True
