# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
# Solution 1, Prefix Sum
class Solution:
    def dfs(self, node, curr, target, d):
        if node is None:
            return
        
        curr += node.val
        self.res += d[curr - target]
        d[curr] += 1
        
        self.dfs(node.left, curr, target, d)
        self.dfs(node.right, curr, target, d)
        d[curr] -= 1
        
        
    def pathSum(self, root: TreeNode, target: int) -> int:
        d = collections.Counter()
        self.res = 0
        d[0] = 1
        self.dfs(root, 0, target, d)
        
        return self.res
        
# Solution 2, Recursion
class Solution:
    
    def dfs(self, node, curr, target):
        if node is None:
            return 0
        res = 0
        if node.val + curr == target:
            res += 1
        curr += node.val
        res += self.dfs(node.left, curr, target)
        res += self.dfs(node.right, curr, target)
        
        return res
    
    def pathSum(self, root: TreeNode, target: int) -> int:
        if root is None:
            return 0
        
        return self.dfs(root, 0, target) + self.pathSum(root.left, target) + self.pathSum(root.right, target)