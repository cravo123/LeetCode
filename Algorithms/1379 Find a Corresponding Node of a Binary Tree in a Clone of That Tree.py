# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, DFS, if tree node values are unique
class Solution:
    def dfs(self, curr, target):
        if curr is None or curr.val == target.val:
            return curr
        
        return self.dfs(curr.left, target) or self.dfs(curr.right, target)
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.dfs(cloned, target)

# Solution 2, if tree node values are not unique
# For each tree node in cloned, check if it has same tree structure as target
class Solution:
    def check_same(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.check_same(p.left, q.left) and self.check_same(p.right, q.right)
    
    def dfs(self, curr, target):
        if self.check_same(curr, target):
            return curr
        
        if curr is None:
            return None
        
        return self.dfs(curr.left, target) or self.dfs(curr.right, target)
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        return self.dfs(cloned, target)