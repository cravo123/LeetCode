# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        
        curr = 0
        
        if node.val % 2 == 0:
            for p in [node.left, node.right]:
                if p:
                    if p.left:
                        curr += p.left.val
                    if p.right:
                        curr += p.right.val

        return curr + self.dfs(node.left) + self.dfs(node.right)
            
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.dfs(root)