# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

# Solution 1, serialize binary tree, note that we need to include
# None node as well. Otherwise two trees with different structures
# could end up same serialization. Here we use '#' to represent 
# None node.
class Solution:
    def dfs(self, node, d):
        if node is None:
            return '#'
        L, R = self.dfs(node.left, d), self.dfs(node.right, d)
        
        curr = ','.join([str(node.val), L, R])
        d[curr].append(node)
        
        return curr
        
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        d = collections.defaultdict(list)
        
        self.dfs(root, d)
        
        res = [d[c][0] for c in d if len(d[c]) > 1]
        
        return res