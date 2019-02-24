# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, Recursion
class Solution:
    def dfs(self, node, target):
        if node is None:
            return False
        target -= node.val
        if node.left is None and node.right is None:
            return target == 0
        
        return self.dfs(node.left, target) or self.dfs(node.right, target)
    
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        return self.dfs(root, target)

# Solution 2, Iteration
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if root is None:
            return False
        q = [[root, target]]
        
        while q:
            p, target = q.pop()
            if p.left is None and p.right is None and p.val == target:
                return True
            target -= p.val
            if p.left:
                q.append([p.left, target])
            if p.right:
                q.append([p.right, target])
        return False