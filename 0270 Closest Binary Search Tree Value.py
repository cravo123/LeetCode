# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, Pre-order traverse BST, update nearest value
# We didn't use BST property in this solution, which means it can be optimized
class Solution:
    def dfs(self, node, target):
        if node is None:
            return
        if abs(node.val - target) < abs(self.res - target):
            self.res = node.val
        
        self.dfs(node.left, target)
        self.dfs(node.right, target)
        
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.res = float('inf')
        
        self.dfs(root, target)
        
        return self.res

# Solution 2, use BST property to trim the traversal path
class Solution:
    def dfs(self, node, target):
        if node is None:
            return
        if abs(node.val - target) < abs(self.res - target):
            self.res = node.val
        
        if node.val < target:
            self.dfs(node.right, target)
        else:
            self.dfs(node.left, target)
        
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.res = float('inf')
        
        self.dfs(root, target)
        
        return self.res

# Solution 2.1, similar recursion idea, but better implementation
class Solution:
    def dfs(self, node, target, curr_res):
        if node is None:
            return curr_res
        
        if abs(node.val - target) < abs(curr_res - target):
            curr_res = node.val
        
        if node.val < target:
            return self.dfs(node.right, target, curr_res)
        return self.dfs(node.left, target, curr_res)
        
    def closestValue(self, root: TreeNode, target: float) -> int:
        return self.dfs(root, target, float('inf'))

# Solution 3, Iteration
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = root.val
        
        curr = root
        while curr:
            if abs(curr.val - target) < abs(res - target):
                res = curr.val
            
            if curr.val <= target:
                curr = curr.right
            else:
                curr = curr.left
        
        return res