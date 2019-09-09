# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
# return once we found a larger value
class Solution:
    def dfs(self, node, curr):
        if node is None:
            return float('inf')
        if node.val > curr:
            return node.val
        return min(self.dfs(node.left, curr), self.dfs(node.right, curr))
        
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        curr = root.val
        
        res = self.dfs(root, curr)
        
        return res if res < float('inf') else -1