# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    def dfs(self, node, seen):
        if node is None:
            return
        seen[node.val] += 1
        
        self.dfs(node.left, seen)
        self.dfs(node.right, seen)
        
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        seen = collections.Counter()
        
        self.dfs(root, seen)
        
        val = max(seen.values())
        res = [c for c in seen if seen[c] == val]
        
        return res