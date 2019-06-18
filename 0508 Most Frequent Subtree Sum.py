# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

# Solution 1, recursion + hashmap
class Solution:
    def dfs(self, node, d):
        if node is None:
            return 0
        L, R = self.dfs(node.left, d), self.dfs(node.right, d)
        v = L + R + node.val
        d[v] += 1
        
        return v
        
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        d = collections.Counter()
        
        self.dfs(root, d)
        
        max_val = max(d.values())
        
        res = [c for c in d if d[c] == max_val]
        
        return res