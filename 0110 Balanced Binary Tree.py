# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion bottom-up O(n)
# A trick is we use -1 to represent tree is not balanced,
# so we can do it in O(n)
class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        
        L, R = self.dfs(node.left), self.dfs(node.right)
        if L < 0 or R < 0 or abs(L - R) > 1:
            return -1
        return max(L, R) + 1
        
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        return self.dfs(root) >= 0

# Solution 2, recursion top-down O(n ^ 2)
# since we traverse each node and check its height
class Solution:
    def depth(self, node):
        if node is None:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        L, R = self.depth(root.left), self.depth(root.right)
        
        return abs(L - R) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)