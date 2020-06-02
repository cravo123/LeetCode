import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1, DFS, back-tracking
class Solution:
    def dfs(self, node, d):
        if node is None:
            return
        d[node.val] += 1
        
        if node.left is None and node.right is None:
            total = sum(d.values())
            odd_total = sum(v % 2 for v in d.values())
            
            if total % 2 == odd_total:
                self.res += 1            
        
        self.dfs(node.left, d)
        self.dfs(node.right, d)
        # back-tracking
        d[node.val] -= 1
        
        
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        d = collections.Counter()
        
        self.res = 0
        
        self.dfs(root, d)
        
        return self.res