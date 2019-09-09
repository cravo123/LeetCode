# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, one-pass with hashmap
class Solution:
    def dfs(self, node, d):
        if node is None:
            return 0
        
        curr = node.val + self.dfs(node.left, d) + self.dfs(node.right, d)
        d[curr] += 1
        
        return curr
        
    def checkEqualTree(self, root: TreeNode) -> bool:
        d = collections.Counter()
        
        total = self.dfs(root, d)
        
        if total == 0:
            return d[total] > 1
        return total % 2 == 0 and total // 2 in d

# Solution 2, Recursion, DFS
# It is a two-pass solution.
#   step 1, calculate total sum of the tree
#   step 2, check if total sum is even and any sub tree sum == total sum // 2
class Solution:
    def tree_sum(self, node):
        if node is None:
            return 0
        return node.val + self.tree_sum(node.left) + self.tree_sum(node.right)
    
    def check(self, node, target):
        if node is None:
            return 0, False
        L, R = self.check(node.left, target), self.check(node.right, target)
        
        if L[1] or R[1] or L[0] + R[0] + node.val == target:
            return None, True
        
        return L[0] + R[0] + node.val, False
    
    def checkEqualTree(self, root: TreeNode) -> bool:
        total = self.tree_sum(root)
        
        if total % 2 != 0:
            return False
        
        L = self.check(root.left, total // 2) 
        R = self.check(root.right, total // 2)
        
        return L[1] or R[1]